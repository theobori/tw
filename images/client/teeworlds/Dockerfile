FROM tw_base_client:latest

# Working directory
ENV DIRNAME client

# Clone the git repository
RUN git clone https://github.com/teeworlds/teeworlds --recurse-submodules $DIRNAME

WORKDIR $DIRNAME

# Compile client only
RUN mkdir -p build && \
    cd build && \
    cmake .. && \
    make teeworlds && \
    cp -r * .. && cd ..

ENTRYPOINT [ "./teeworlds"]
