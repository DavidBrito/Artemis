#!/bin/bash

set -e

source .venv/bin/activate

current_dir=$(pwd)
server_pid=""

cleanup() {
    if [ -n "$server_pid" ]; then
        echo "Stopping Flask server..."
        kill "$server_pid"
    fi
}

trap cleanup EXIT

FLASK_APP_DIR="$current_dir/api" python3 api/server.py &
server_pid=$!

sleep 2

python3 main.py
