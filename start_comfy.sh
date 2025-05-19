#!/bin/zsh
export MPS_GRAPHICS_DEVICE=discrete
nohup python3 main.py --gpu-only --port 8190 >> runtime.log 2>&1 &
echo "ComfyUI started at http://localhost:8190"