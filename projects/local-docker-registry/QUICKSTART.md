# Local Docker Registry - Quick Start Guide

Get a local Docker registry up and running in 5 minutes.

## Prerequisites

- Docker and Docker Compose installed
- 10GB+ free disk space for image storage
- Network connectivity (host only for development)

## Quick Start (5 minutes)

### Step 1: Start Registry

```bash
docker-compose up -d
```

This starts:
- **Registry API:** http://localhost:5000 (stores images)
- **Registry UI:** http://localhost:8080 (browse images)

### Step 2: Verify It Works

```bash
# Check services are running
docker-compose ps

# Test registry API
curl http://localhost:5000/v2/

# Should return: {}
```

### Step 3: Push Your First Image

```bash
# Build or get an image
docker build -t myapp:latest .

# Tag for local registry
docker tag myapp:latest localhost:5000/myapp:latest

# Push to registry
docker push localhost:5000/myapp:latest

# Verify it's there
curl http://localhost:5000/v2/_catalog | jq .
```

Output should include your image.

### Step 4: Pull from Registry

```bash
# On same machine or another machine on network
docker pull localhost:5000/myapp:latest

# Or from network hostname
docker pull registry-host:5000/myapp:latest
```

### Step 5: Browse Images (Optional)

Open browser to: http://localhost:8080

- Search images
- View layers and metadata
- Delete images (if enabled)

---

## Common Tasks

### List All Images

```bash
curl http://localhost:5000/v2/_catalog | jq '.repositories[]'
```

### Get Image Digest (for deletion)

```bash
# Get manifest digest for specific tag
curl http://localhost:5000/v2/myapp/manifests/latest \
  -H "Accept: application/vnd.docker.distribution.manifest.v2+json"

# Note the Docker-Content-Digest header
```

### Delete Image

```bash
# Method 1: Using digest
DIGEST="sha256:abc123..."
curl -X DELETE http://localhost:5000/v2/myapp/manifests/$DIGEST

# Method 2: Using UI
# Visit http://localhost:8080 and use delete button
```

### Check Disk Usage

```bash
# View registry storage
docker volume inspect local-docker-registry_registry_data

# Or check filesystem
du -sh $(docker volume inspect -f '{{ .Mountpoint }}' \
  local-docker-registry_registry_data)
```

### Run Garbage Collection

```bash
# Remove unused image layers
docker-compose exec registry \
  registry garbage-collect \
  /etc/docker/registry/config.yml --delete-untagged
```

### View Logs

```bash
# Registry logs
docker-compose logs -f registry

# UI logs
docker-compose logs -f registry-ui

# Both
docker-compose logs -f
```

---

## Mirror Popular Images

Pull and cache public images locally:

```bash
#!/bin/bash
# mirror-images.sh - Mirror popular base images

IMAGES=(
  "node:20-alpine"
  "node:20-slim"
  "ubuntu:22.04"
  "alpine:latest"
  "python:3.11-alpine"
  "golang:1.21-alpine"
)

for image in "${IMAGES[@]}"; do
  echo "Mirroring $image..."
  docker pull docker.io/$image
  docker tag docker.io/$image localhost:5000/$image
  docker push localhost:5000/$image
  docker rmi docker.io/$image  # Optional: free space
done

echo "Done!"
```

Usage:
```bash
chmod +x mirror-images.sh
./mirror-images.sh
```

---

## Integration Examples

### Docker Compose

Use registry in your docker-compose.yml:

```yaml
services:
  myapp:
    image: localhost:5000/myapp:latest  # Use local registry
    build:
      context: .
      dockerfile: Dockerfile
```

Run:
```bash
docker-compose up
```

### Kubernetes / k3s

Configure k3s to use local registry:

```bash
# Edit /etc/rancher/k3s/registries.yaml
mirrors:
  docker.io:
    endpoint:
      - "http://registry-host:5000"
  localhost:5000:
    endpoint:
      - "http://registry-host:5000"
```

Then use in deployments:
```yaml
spec:
  containers:
    - image: localhost:5000/myapp:latest
      name: myapp
```

### CI/CD Pipeline

```bash
# In your CI/CD script

# Build image
docker build -t myapp:$BUILD_ID .

# Push to local registry
docker tag myapp:$BUILD_ID localhost:5000/myapp:$BUILD_ID
docker push localhost:5000/myapp:$BUILD_ID

# Deploy (pulls from local registry, no bandwidth cost)
docker run localhost:5000/myapp:$BUILD_ID
```

---

## Troubleshooting

### "Connection refused" on docker push/pull

**Problem:** Registry not accessible

**Solutions:**
```bash
# Check if running
docker-compose ps

# Check if port 5000 is listening
netstat -an | grep 5000

# Restart
docker-compose restart registry

# Check logs
docker-compose logs registry
```

### "Received unexpected EOF" when pushing

**Problem:** Registry volume full

**Solutions:**
```bash
# Check disk usage
du -sh $(docker volume inspect -f '{{ .Mountpoint }}' \
  local-docker-registry_registry_data)

# Free space: remove old images or run GC
docker-compose exec registry \
  registry garbage-collect \
  /etc/docker/registry/config.yml --delete-untagged

# Or increase disk space
```

### UI not responding (http://localhost:8080)

**Problem:** UI container down

**Solutions:**
```bash
# Check status
docker-compose ps registry-ui

# Restart
docker-compose restart registry-ui

# View logs
docker-compose logs registry-ui
```

### Image pull slow

**Problem:** Network bottleneck or image not cached

**Solutions:**
- Pull again (should be cached)
- Check network connectivity: `ping registry-host`
- Monitor with: `docker-compose logs -f registry`
- Verify image is actually in registry: `curl http://localhost:5000/v2/_catalog`

---

## Stop & Cleanup

### Stop Registry (keeps data)

```bash
docker-compose stop
```

Resume later:
```bash
docker-compose start
```

### Remove Registry (keeps data volume)

```bash
docker-compose down
```

Restart:
```bash
docker-compose up -d
```

### Complete Cleanup (WARNING: deletes all images)

```bash
docker-compose down -v
```

---

## Performance Tips

1. **Use SSD Storage**
   - Registry is I/O intensive
   - Move storage to fast disk if possible

2. **Enable Caching**
   - Already enabled in docker-compose.yml
   - `REGISTRY_STORAGE_CACHE_BLOBDESCRIPTOR: inmemory`

3. **Regular Cleanup**
   - Run garbage collection weekly
   - Automate with cron or scheduler

4. **Monitor Disk Usage**
   - Set alerts at 75% full
   - Plan for 2-3x growth

5. **Network Optimization**
   - Use host network for fastest access
   - Or custom bridge for cleaner setup

---

## Advanced Configuration

See [README.md](README.md) for:
- TLS/HTTPS setup
- Authentication (htpasswd, OAuth2)
- Image retention policies
- Monitoring and metrics
- Multi-host setup
- S3/Azure backend storage

---

## Next Steps

1. Set up mirror images: `./mirror-images.sh`
2. Integrate with projects (DevOps Cluster, Cline, k3s)
3. Configure monitoring and alerts
4. Automate cleanup with cron jobs
5. Set up backup strategy for registry data

---

**Status:** Ready to use
**Last Updated:** 2026-01-16

