FROM alpine:latest

# Working/server directory name
ENV DIRNAME fng2

# Install dependencies to build binaries
RUN apk update && \
	apk --update add --no-cache --virtual .build-dependencies git cmake make gcc g++ alpine-sdk \
	sdl2 sdl2-dev python3 \
    freeglut freeglut-dev glew-dev glm-dev && \
    ln -sf python3 /usr/bin/python && \
	apk --update --no-cache add build-base && \
    git clone https://github.com/Jupeyy/teeworlds-fng2-mod.git --branch fng_06 $DIRNAME && \
    cd $DIRNAME && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j16 && \
    cp -r * .. && cd ..

WORKDIR $DIRNAME

ENTRYPOINT [ "sh", "start.sh" ]


# Default configuration
# docker run -it -p 8303:8303/udp fng


# Custom configuration
# You need a cfg file named `fng.cfg`
# docker run -it -v $PWD/fng.cfg:/fng2/fng.cfg -p 8303:8303/udp fng