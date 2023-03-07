FROM tw_base:latest

ENV DIRNAME fng2

# Cloning the repository
RUN git clone https://github.com/Jupeyy/teeworlds-fng2-mod.git --branch fng_06 $DIRNAME

# Building
RUN cd $DIRNAME && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j16 && \
    cp -r * .. && cd ..

WORKDIR $DIRNAME

COPY server.cfg $DIRNAME

ENTRYPOINT [ "sh", "start.sh" ]
