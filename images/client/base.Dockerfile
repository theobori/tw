FROM ubuntu:20.04

# Avoid tz stuck at installation
ONBUILD ARG DEBIAN_FRONTEND=noninteractive
ONBUILD ENV TZ=Europe/Moscow

# Install dependencies to build binaries
ONBUILD RUN apt-get update && apt-get upgrade -y
ONBUILD RUN apt-get -y install build-essential \
    cmake \
    git \
    libfreetype6-dev \
    libsdl2-dev \
    libpnglite-dev \
    libwavpack-dev \
    python3
