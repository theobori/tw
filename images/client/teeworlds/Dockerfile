FROM tw_base_client:latest

# Working directory
ENV DIRNAME client
ENV BUILD_DIR ${DIRNAME}_build
ENV CONFIG autoexec.cfg

# Clone the git repository
RUN git clone https://github.com/teeworlds/teeworlds --recurse-submodules $BUILD_DIR

WORKDIR $BUILD_DIR

# Compile client only
RUN mkdir -p build && \
    cd build && \
    cmake .. && \
    make teeworlds && \
    mkdir -p /$DIRNAME && \
    mv * /$DIRNAME

WORKDIR /$DIRNAME

RUN rm -rf /$BUILD_DIR

ENTRYPOINT [ "./teeworlds"]
