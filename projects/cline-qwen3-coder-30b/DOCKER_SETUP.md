# Docker Setup Guide: Cline with Local Ollama

Complete setup guide for running Cline CLI in Docker with local Ollama inference, similar to how Claude Code is launched.

## Quick Start (Windows)

```batch
REM 1. Start Ollama (if not already running)
ollama serve

REM 2. In another terminal, run the launcher
cline-launch.bat

REM 3. (Optional) Specify a different model
cline-launch.bat qwen2:14b
```

## Quick Start (Linux/macOS)

```bash
# 1. Start Ollama (if not already running)
ollama serve

# 2. In another terminal, run the launcher
chmod +x cline-launch.sh
./cline-launch.sh

# 3. (Optional) Specify a different model
./cline-launch.sh qwen2:14b
```

## Detailed Setup Steps

### Step 1: Install Prerequisites

**Windows:**
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop) (includes Docker CLI)
- Install [Ollama](https://ollama.ai/) or run in Docker

**Linux:**
```bash
# Ubuntu/Debian
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh
```

**macOS:**
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
- Install [Ollama](https://ollama.ai/)

### Step 2: Start Ollama Server

Ollama must be running on the host machine before launching Cline. It will serve models via REST API on port 11434.

```bash
ollama serve
```

Or run in Docker:
```bash
docker-compose up -d ollama
```

Check that Ollama is accessible:
```bash
curl http://localhost:11434/api/tags
```

Should return JSON with list of installed models.

### Step 3: Download Model to Ollama

In a new terminal, pull the desired model:

```bash
# Primary: Qwen3 Coder 30b 4-bit (~15GB)
ollama pull qwen3-coder

# Fallback options (faster inference, lower quality)
ollama pull qwen2:14b    # ~10GB
ollama pull qwen2:7b     # ~5GB
```

Verify model is available:
```bash
ollama list
```

### Step 4: Build Cline Docker Image

In the project directory (where `Dockerfile` is located):

```bash
docker build -t cline-local .
```

This creates a Docker image with:
- Node.js 20
- Cline CLI pre-installed
- Git and build tools for code operations
- Workspace volume mount point at `/workspace`

### Step 5: Launch Cline

**Option A: Using provided launcher scripts (Recommended)**

Windows:
```batch
cline-launch.bat
```

Linux/macOS:
```bash
./cline-launch.sh
```

**Option B: Manual Docker command**

Windows (cmd):
```batch
docker run -it --rm ^
  -v "%CD%":/workspace ^
  -e OLLAMA_API_URL=http://host.docker.internal:11434 ^
  cline-local
```

Windows (PowerShell):
```powershell
docker run -it --rm `
  -v "$pwd":/workspace `
  -e OLLAMA_API_URL=http://host.docker.internal:11434 `
  cline-local
```

Linux/macOS:
```bash
docker run -it --rm \
  -v "$PWD":/workspace \
  -e OLLAMA_API_URL=http://host.docker.internal:11434 \
  cline-local
```

## How It Works

### Container Architecture

```
┌─────────────────────────────────────────┐
│         Docker Container                │
│  ┌──────────────────────────────────┐   │
│  │  Node.js 20                      │   │
│  │  ├─ Cline CLI                    │   │
│  │  └─ npm/build tools              │   │
│  └──────────────────────────────────┘   │
│  ┌──────────────────────────────────┐   │
│  │  Volume Mount                    │   │
│  │  Host: %CD% → Container: /workspace│   │
│  │  (all file operations)           │   │
│  └──────────────────────────────────┘   │
│                                          │
│  Environment:                            │
│  OLLAMA_API_URL=http://host.docker.internal:11434│
└─────────────────────────────────────────┘
                    ↓
        ┌──────────────────────┐
        │   Host Machine       │
        │  ┌────────────────┐  │
        │  │ Ollama Server  │  │
        │  │ Port 11434     │  │
        │  │                │  │
        │  │ Qwen3 Model    │  │
        │  │ Running on GPU │  │
        │  │ (RTX 4070 Ti)  │  │
        │  └────────────────┘  │
        │  ┌────────────────┐  │
        │  │ Current Dir    │  │
        │  │ (workspace)    │  │
        │  └────────────────┘  │
        └──────────────────────┘
```

### Key Technical Details

- **Isolation:** Container keeps host system clean
- **Workspace Mount:** `-v %CD%:/workspace` maps current directory into container
- **Host Access:** `host.docker.internal` allows container to reach host services
- **GPU Passthrough:** Ollama on host has direct GPU access (faster than containerized GPU)
- **Ephemeral:** `--rm` automatically deletes container after exit
- **Interactive:** `-it` provides interactive terminal for Cline CLI

## Environment Variables

| Variable | Default | Purpose |
|----------|---------|---------|
| `OLLAMA_API_URL` | `http://host.docker.internal:11434` | Endpoint for Cline to find Ollama |
| `OLLAMA_MODEL` | (none) | Optional: specify model for Cline to use |
| `NODE_ENV` | `production` | Node.js environment |

Override in launcher:
```bash
docker run -it --rm \
  -v %CD%:/workspace \
  -e OLLAMA_API_URL=http://host.docker.internal:11434 \
  -e OLLAMA_MODEL=qwen2:14b \
  cline-local
```

## Performance Monitoring

While Cline is running, monitor in separate terminal:

**GPU Memory (RTX 4070 Ti - 12GB):**
```bash
nvidia-smi -l 1
```

**Docker Container Stats:**
```bash
docker stats cline-local
```

**Ollama Logs:**
```bash
# If running directly
# (check console where ollama serve is running)

# If running in docker-compose
docker-compose logs -f ollama
```

## Troubleshooting

### Docker not found
```
ERROR: Docker not found
```
→ Install [Docker Desktop](https://www.docker.com/products/docker-desktop)

### OLLAMA_API_URL connection refused
```
ERROR: Cannot connect to http://host.docker.internal:11434
```
→ Ensure Ollama is running: `ollama serve` in another terminal

### Model not found
```
ERROR: model qwen3-coder not found
```
→ Pull the model first: `ollama pull qwen3-coder`

### Out of Memory (CUDA Out of Memory)
```
CUDA out of memory
```
→ Try smaller model: `ollama pull qwen2:7b`
→ Or reduce context window in Cline prompts

### GPU not used by Ollama
```
GPU utilization: 0%
```
→ Verify NVIDIA GPU driver: `nvidia-smi`
→ Restart Ollama: `killall ollama && ollama serve`

### Container can't write to workspace
```
Permission denied: /workspace/...
```
→ Linux only: May need `docker run --user $(id -u):$(id -g)`

## Alternative: Using Docker Compose

For more complex setups with persistent Ollama:

```bash
# Start Ollama as background service
docker-compose up -d ollama

# Pull model into running container
docker-compose exec ollama ollama pull qwen3-coder

# In separate terminal, launch Cline
./cline-launch.sh
```

See `docker-compose.yml` for service configuration.

## Tips & Tricks

### Create Permanent Alias/Function

**PowerShell Profile (Windows):**
```powershell
function cline-docker {
    param([string]$Model = "qwen3-coder")
    docker run -it --rm `
      -v "$pwd":/workspace `
      -e OLLAMA_API_URL=http://host.docker.internal:11434 `
      -e OLLAMA_MODEL=$Model `
      cline-local
}
```

Add to: `$PROFILE` (usually `Documents\PowerShell\profile.ps1`)

**Bash Profile (Linux/macOS):**
```bash
function cline-docker() {
    local model="${1:-qwen3-coder}"
    docker run -it --rm \
      -v "$PWD":/workspace \
      -e OLLAMA_API_URL=http://host.docker.internal:11434 \
      -e OLLAMA_MODEL="$model" \
      cline-local
}
```

Add to: `~/.bashrc` or `~/.zshrc`

### Use Different Models for Different Tasks

```bash
# Quick iteration (fast)
./cline-launch.sh qwen2:7b

# Balanced
./cline-launch.sh qwen2:14b

# High quality (slow)
./cline-launch.sh qwen3-coder
```

### Persistent Container (Keep Running)

For long-running development sessions:
```bash
# Start persistent container
docker run -id --name cline-session \
  -v %CD%:/workspace \
  -e OLLAMA_API_URL=http://host.docker.internal:11434 \
  cline-local sleep infinity

# Attach to it
docker exec -it cline-session bash

# Later, stop it
docker stop cline-session
docker rm cline-session
```

## Next Steps

1. Build the image: `docker build -t cline-local .`
2. Start Ollama: `ollama serve`
3. Pull a model: `ollama pull qwen3-coder`
4. Launch Cline: `./cline-launch.sh` (or `.bat` on Windows)
5. Test: Ask Cline to generate a simple function
6. Monitor: Watch `nvidia-smi` to see model performance

## References

- [Docker Documentation](https://docs.docker.com/)
- [Ollama GitHub](https://github.com/ollama/ollama)
- [Cline GitHub](https://github.com/cline/cline)
- [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-docker) (for GPU in containers)

---

**Created:** 2026-01-16
**Status:** Ready for testing
