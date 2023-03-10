FROM ubuntu:latest

ONBUILD RUN apt update -y && apt upgrade -y

ONBUILD RUN apt install -y \
    build-essential \
    cmake \
    make \
    git \
    libfreetype6-dev \
    libsdl2-dev \
    libpnglite-dev \
    libwavpack-dev \
    python3
