#!/bin/bash
# docker run -p 5000:5000 digits:v1
# podman run -p 5000:5000 digits:v1


docker build -t digits:v1 -f docker/Dockerfile .

# rm models/*
# ls -lh models

echo "Run docker image"
docker run -v ./models:/digits/models digits:v1


# echo "List Models"
# ls -lh models
