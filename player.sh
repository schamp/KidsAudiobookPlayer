#!/bin/bash

#export LD_LIBRARY_PATH=/usr/local/lib/python3.2/dist-packages/PySide:$LD_LIBRARY_PATH
python3 ./player.py -a localhost -l /home/pi/Music $*
