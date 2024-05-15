#!/bin/bash

mkdir -p .cache
docker run -it --rm --gpus=all -v $(pwd)/.cache:/root/.cache -v $(pwd):/app -w /app mexxik/audiocraft-demo