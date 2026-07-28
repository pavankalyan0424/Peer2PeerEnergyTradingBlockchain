#!/bin/bash

docker run --rm -it -v $(pwd)/../blockchain_docker:/workspace -w /workspace enerchain-dev
#docker run --rm -it -v $(pwd)/..:/workspace -w /workspace enerchain-dev
