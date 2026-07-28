FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

# Install basic tools
RUN apt-get update && apt-get install -y \
	curl \
	git \
	build-essential \
	libssl-dev \
	pkg-config \
	ca-certificates \
	vim \
	&& rm -rf /va/lib/apt/lists/*

# Install Foundry and set paths
RUN curl -L https://foundry.paradigm.xyz | bash
ENV PATH="/root/.foundry/bin:${PATH}"
RUN foundryup

CMD ["/bin/bash"]
