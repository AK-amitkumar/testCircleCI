#!/bin/bash



#First we pull our Docker image so the next build becomes faster
docker pull $DOCKER_URL:latest

# Then we build again or image
docker build --rm=false --cache-from $DOCKER_URL:latest -t bca_master -f Dockerfile.aws .
