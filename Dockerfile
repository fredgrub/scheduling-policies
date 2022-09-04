# Set up development enviroment with SimGrid and python3 + pip. Depends on Dockerfile.simgrid 
# image (named as simgrid-v3_13).
# 
# 1. Install python3 + pip, project dependencies and useful tools.
# 
# By: Lucas de Sousa Rosa <roses.lucas404@gmail.com>
# Created: 2022/09/04 19:43 by @fredgrub

FROM simgrid-v3_13

# Install python3 and useful tools
RUN apt-get update
RUN apt install -y \
    python3 \
    python3-pip \
    wget \
    vim

# Ensure pip is updated
RUN python3 -m pip install --upgrade pip setuptools wheel

# Install python packages
RUN python3 -m pip install \
    numpy \
    scipy \
    matplotlib \
    seaborn \
    statsmodels \
    sklearn