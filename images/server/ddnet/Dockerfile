FROM tw_base_server:latest

ENV DIRNAME server
ENV BUILD_DIR ${DIRNAME}_build
ENV CONFIG autoexec.cfg

RUN apt install -y \
    cargo \
    glslang-tools \
    google-mock \
    libavcodec-extra \
    libavdevice-dev \
    libavfilter-dev \
    libavformat-dev \
    libavutil-dev \
    libcurl4-openssl-dev \
    libglew-dev \
    libnotify-dev \
    libogg-dev \
    libopus-dev \
    libopusfile-dev \
    libpng-dev \
    libsqlite3-dev \
    libssl-dev \
    libvulkan-dev \
    libx264-dev \
    rustc \
    libmariadb-dev \
    libgtest-dev \
    spirv-tools

# Cloning the repository
RUN git clone --recursive https://github.com/ddnet/ddnet $BUILD_DIR

WORKDIR $BUILD_DIR

# Building
RUN mkdir -p build && \
    cd build && \
    cmake -DMYSQL=ON .. && \
    make && \
    mkdir -p /$DIRNAME && \
    mv DDNet-Server ../data /$DIRNAME

WORKDIR /$DIRNAME

RUN rm -rf /$BUILD_DIR
RUN rm -f data/autoexec_server.cfg

COPY $CONFIG $CONFIG

ENTRYPOINT [ "./DDNet-Server" ]
