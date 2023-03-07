FROM alpine:latest

# Install dependencies to build binaries
ONBUILD RUN apk update && apk --update add --no-cache --virtual .build-dependencies \
    git \
    cmake \
    make \
    gcc \
    g++ \
    alpine-sdk \
    sdl2 \
    sdl2-dev \
    python3 \
    freeglut \
    freeglut-dev \
    glew-dev \
    glm-dev \
    build-base

# Symlink python
ONBUILD RUN ln -sf python3 /usr/bin/python
