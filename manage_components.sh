#!/bin/bash

set -e

source .venv/bin/activate

current_dir=$(pwd)
server_pid=""
interface_pid=""

start_flask_server() {
    FLASK_APP_DIR="$current_dir/api" python3 api/server.py &
    server_pid=$!
    echo "Flask server started with PID $server_pid"
    sleep 2
}

start_interface() {
    python3 main.py &
    interface_pid=$!
    echo "Interface started with PID $interface_pid"
}

stop_flask_server() {
    echo "Stopping Flask server..."
    
    # Use pkill to find and terminate the Flask server process
    pkill -f "python3 api/server.py"
    
    echo "Flask server stopped."
}

stop_interface() {
    if [ -n "$interface_pid" ]; then
        echo "Stopping Interface..."
        kill "$interface_pid"
        wait "$interface_pid"
        echo "Interface stopped."
        interface_pid=""
    fi
}

cleanup() {
    echo "Cleaning up..."
    stop_interface
    stop_flask_server
}

trap cleanup EXIT  # This will call the cleanup function when the script exits

case "$2" in
    "all")
        case "$1" in
            "start")
                start_flask_server
                start_interface
                ;;
            "stop")
                cleanup
                ;;
            *)
                echo "Usage: $0 {start|stop} {all|api|interface}"
                exit 1
                ;;
        esac
        ;;
    "api")
        case "$1" in
            "start")
                start_flask_server
                ;;
            "stop")
                stop_flask_server
                ;;
            *)
                echo "Usage: $0 {start|stop} {all|api|interface}"
                exit 1
                ;;
        esac
        ;;
    "interface")
        case "$1" in
            "start")
                start_interface
                ;;
            "stop")
                stop_interface
                ;;
            *)
                echo "Usage: $0 {start|stop} {all|api|interface}"
                exit 1
                ;;
        esac
        ;;
    *)
        echo "Usage: $0 {start|stop} {all|api|interface}"
        exit 1
        ;;
esac
