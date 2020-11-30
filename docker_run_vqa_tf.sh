#!/usr/bin/env bash

#    -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY \
#    -v /home/jiahuei/Documents/1_TF_files:/master/experiments \

#    -p 6006:6006 \

CODE_ROOT="/home/jiahuei/Documents/bottom-up-attention-tf/"
DOC_DIR="/home/jiahuei/Documents"

docker run -it \
    --gpus all \
    -v ${CODE_ROOT}:/master/src \
    -v ${DOC_DIR}/3_Datasets/mscoco:/mscoco \
    -u "$(id -u)":"$(id -g)" \
    -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY="$DISPLAY" \
    --rm jiahuei/tensorflow:1.13.2-gpu-py3

