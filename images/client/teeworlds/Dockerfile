FROM tw_base_client:latest

# Working directory
ENV DIRNAME tw

# Clone the git repository
RUN git clone https://github.com/teeworlds/teeworlds --recurse-submodules $DIRNAME

WORKDIR $DIRNAME

# Compile client only
RUN mkdir -p build && \
    cd build && \
    cmake .. && \
    make teeworlds

# Not working if running the executable outside the build directory
WORKDIR build

ENTRYPOINT [ "./teeworlds"]
