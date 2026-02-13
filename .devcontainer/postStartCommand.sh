#!/usr/bin/env bash
set -euo pipefail

cd /workspaces/app/frontend

# 如果 node_modules 不存在，补一次 install（首次或依赖变更）
if [ ! -d node_modules ]; then
  npm install
fi

# 如果 5174 已经有人在跑，就不重复启动
if lsof -iTCP:5174 -sTCP:LISTEN -n -P >/dev/null 2>&1; then
  echo "Frontend already running on 5174"
  exit 0
fi

# 启动前端（后台）
nohup npm run dev -- --host 0.0.0.0 --port 5174 --strictPort >/tmp/frontend.log 2>&1 &
echo "Started frontend on 5174 (logs: /tmp/frontend.log)"
