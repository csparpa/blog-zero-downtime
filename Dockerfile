FROM python:3.5
MAINTAINER Claudio Sparpaglione <csparpa@gmail.com>

# Utilities
RUN apt-get update && \
    apt-get install -y ipython3 vim

# Create a no-ops startup script
RUN mkdir /hcr && \
    touch /hcr/run.sh
VOLUME /hcr

# Run the startup script
WORKDIR /hcr
CMD cd /hcr && \
    bash run.sh && \
    tail -f /dev/null

EXPOSE 1234
