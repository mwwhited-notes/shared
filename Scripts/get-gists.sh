#!/bin/bash

USERNAME=mwwhited  # Replace with your GitHub username
GIST_API="https://api.github.com/users/$USERNAME/gists?per_page=100"

echo "$GIST_API"

# Get list of gist clone URLs
curl -s "$GIST_API" | grep '"git_pull_url":' | cut -d '"' -f 4 | while read url; do
  # Extract the gist ID from the URL
  gist_id=$(basename "$url" .git)

  if [ -d "$gist_id/.git" ]; then
    echo "Updating existing gist: $gist_id"
    (
      cd "$gist_id" && git pull --all || echo "Failed to update $gist_id"
    )
  else
    echo "Cloning new gist: $gist_id"
    git clone "$url" || echo "Failed to clone $gist_id"
  fi
done

