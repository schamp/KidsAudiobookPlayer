#!/bin/bash

sudo sh -c "echo 252 > /sys/class/gpio/export"
sudo sh -c "echo 'out' > /sys/class/gpio/gpio252/direction"
sudo sh -c "echo '1' > /sys/class/gpio/gpio252/value"

