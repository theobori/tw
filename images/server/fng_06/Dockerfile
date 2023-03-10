FROM alpine:latest

ENV DIRNAME server
ENV BUILD_DIR ${DIRNAME}_build
ENV CONFIG autoexec.cfg

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

# Cloning the repository
RUN git clone https://github.com/Jupeyy/teeworlds-fng2-mod.git --branch fng_06 $BUILD_DIR

WORKDIR $BUILD_DIR

# Building
RUN mkdir -p build && \
    cd build && \
    cmake .. && \
    make && \
    mkdir -p /$DIRNAME && \
    mv fng2_srv ../data ../start.sh /$DIRNAME

WORKDIR /$DIRNAME

# Prevention
RUN rm -f fng.cfg
RUN rm -rf /$BUILD_DIR

COPY $CONFIG $CONFIG

ENTRYPOINT [ "sh", "start.sh" ]
