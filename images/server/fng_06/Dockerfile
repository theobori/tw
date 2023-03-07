FROM alpine:latest

# Install dependencies to build binaries
RUN apk update && apk --update add --no-cache --virtual .build-dependencies \
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
RUN ln -sf python3 /usr/bin/python

ENV DIRNAME fng2

# Cloning the repository
RUN git clone https://github.com/Jupeyy/teeworlds-fng2-mod.git --branch fng_06 $DIRNAME

WORKDIR $DIRNAME

# Building
RUN mkdir -p build && \
    cd build && \
    cmake .. && \
    make && \
    cp -r * .. && cd ..

COPY server.cfg fng.cfg

ENTRYPOINT [ "sh", "start.sh" ]
