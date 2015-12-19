#!/bin/bash

echo "Starting screensaver..."
screen -d -m -S screensaver xscreensaver
echo "Starting screensaver blank watcher..."
screen -d -m -S screensaver-watch ./screensaver-watch.pl
echo "Starting player..."
screen -m -S player ./player.sh
