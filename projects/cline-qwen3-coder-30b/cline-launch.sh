#!/bin/bash
# Cline CLI launcher for Linux/macOS with Docker + Ollama
# Usage: ./cline-launch.sh [optional: model name]
#
# Assumes:
# - Docker is installed
# - Ollama is running on host (ollama serve)
# - cline-local image is built (docker build -t cline-local .)

set -e

# Model selection (default to qwen3-coder)
MODEL="${1:-qwen3-coder}"

# Current working directory
WORKSPACE="$(pwd)"

# Detect host address for Docker
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    OLLAMA_HOST="host.docker.internal"
    DOCKER_CMD="docker"
else
    # Linux - need to use host IP or network_mode
    OLLAMA_HOST="host.docker.internal"
    DOCKER_CMD="docker"
fi

echo ""
echo "===================================="
echo "Launching Cline with Local Ollama"
echo "===================================="
echo "Workspace: $WORKSPACE"
echo "Model: $MODEL"
echo "Working directory will be mapped to /workspace in container"
echo ""
echo "Prerequisites:"
echo "  - Docker installed"
echo "  - Ollama server running on host (ollama serve)"
echo "  - Model already pulled (ollama pull $MODEL)"
echo ""

# Check if Docker is available
if ! command -v docker &> /dev/null; then
    echo "ERROR: Docker not found. Install Docker and try again."
    exit 1
fi

# Check if cline-local image exists, if not build it
if ! docker image inspect cline-local &> /dev/null; then
    echo "Building cline-local Docker image..."
    docker build -t cline-local .
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to build Docker image"
        exit 1
    fi
fi

# Launch Cline in Docker with workspace mounted
echo "Starting Cline CLI..."
echo ""

docker run -it --rm \
  -v "$WORKSPACE":/workspace \
  -e OLLAMA_API_URL="http://${OLLAMA_HOST}:11434" \
  -e OLLAMA_MODEL="$MODEL" \
  cline-local

echo ""
echo "Cline session ended."
echo ""
