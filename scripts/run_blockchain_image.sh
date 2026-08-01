#!/bin/bash

docker run -p 8545:8545 --rm -it -v $(pwd)/../blockchain:/workspace -w /workspace enerchain-dev 
