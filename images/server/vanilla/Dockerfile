FROM tw_base_server:latest

ENV DIRNAME server

# Cloning the repository
RUN git clone https://github.com/teeworlds/teeworlds.git $DIRNAME --recurse-submodules

WORKDIR $DIRNAME

RUN git submodule update --init

# Building
RUN mkdir -p build && \
    cd build && \
    cmake .. && \
    make teeworlds_srv && \
    cp -r * .. && cd ..

ENTRYPOINT [ "./teeworlds_srv" ]
