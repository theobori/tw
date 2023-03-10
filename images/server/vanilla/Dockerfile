FROM tw_base_server:latest

ENV DIRNAME server
ENV BUILD_DIR ${DIRNAME}_build
ENV CONFIG autoexec.cfg

# Cloning the repository
RUN git clone https://github.com/teeworlds/teeworlds.git $BUILD_DIR --recurse-submodules

WORKDIR $BUILD_DIR

RUN git submodule update --init

# Building
RUN mkdir -p build && \
    cd build && \
    cmake .. && \
    make teeworlds_srv && \
    mkdir -p /$DIRNAME && \
    mv teeworlds_srv ../data /$DIRNAME

WORKDIR /$DIRNAME

ENTRYPOINT [ "./teeworlds_srv" ]
