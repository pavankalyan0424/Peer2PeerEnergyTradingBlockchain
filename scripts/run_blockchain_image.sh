#!/bin/bash

#docker run --rm -it -v $(pwd)/../blockchain_docker:/workspace -w /workspace enerchain-dev
docker run -p 8545:8545 --rm -it -v $(pwd)/../blockchain_docker:/workspace -w /workspace enerchain-dev 
#docker run --rm -it -v $(pwd)/..:/workspace -w /workspace enerchain-dev
