#!/usr/bin/env bash
set -euo pipefail

# 让 workspace 容器里也能直接跑测试/装依赖（方便 Continue Agent 跑命令）
python -m pip install --upgrade pip
pip install -r backend/requirements.txt

cd frontend
npm install
