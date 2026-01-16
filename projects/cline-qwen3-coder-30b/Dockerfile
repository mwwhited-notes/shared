# Cline CLI with Local Ollama Integration
# Usage: docker build -t cline-local .
# Then: docker run -it --rm -v %CD%:/workspace -e OLLAMA_API_URL=http://host.docker.internal:11434 cline-local

FROM node:20-slim

WORKDIR /app

# Install git and other essentials for Cline operations
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    python3 \
    && rm -rf /var/lib/apt/lists/*

# Install Cline CLI
RUN npm install -g @cline/cli

# Default workspace directory (override with -v mount)
VOLUME ["/workspace"]
WORKDIR /workspace

# Environment variables
ENV OLLAMA_API_URL=http://host.docker.internal:11434
ENV NODE_ENV=production

# Launch Cline with working directory as workspace
ENTRYPOINT ["cline"]
