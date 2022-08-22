FROM ubuntu:18.04

# Install build packages and tools
RUN apt-get update -yq
RUN apt-get install -yq git python3 python3-pip gcc-4.8 g++-4.8 g++ cmake libboost-context-dev libboost-dev doxygen transfig

# Fix tzdata issue
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Sao_Paulo

# Install dependencies
RUN apt-get install -yq python3-numpy python3-scipy python3-matplotlib python3-seaborn python3-sklearn python3-statsmodels

# Build environment variables
ARG BUILD_ROOT=/opt
ARG TARGET_DIR=/opt/simgrid
ARG CLONE_DIR=simgrid-313
ARG SIMGRID_URL=https://framagit.org/simgrid/simgrid.git
ARG SIMGRID_VERSION=v3_13

# Preparation
WORKDIR ${BUILD_ROOT}
RUN mkdir /usr/src/dev
RUN ln -s ${CLONE_DIR} ${TARGET_DIR}

# Clone and build
RUN git clone -b ${SIMGRID_VERSION} --single-branch ${SIMGRID_URL} ${CLONE_DIR}

WORKDIR ${TARGET_DIR}
RUN cmake -DBUILD_SHARED_LIBS=OFF -DCMAKE_INSTALL_PREFIX=${TARGET_DIR}
RUN make
RUN make check
RUN make install
RUN ln -s /opt/simgrid/lib/libsimgrid.so /usr/lib/libsimgrid.so
RUN ln -s /opt/simgrid/lib/libsimgrid.so.3.13 /usr/lib/libsimgrid.so.3.13