#!/bin/bash

# Do some basic checks

if [ "27" = "" ]
then
  echo "Usage: 0 gpio"
  exit 1
fi

# Check if gpio is already exported

if [ ! -d /sys/class/gpio/gpio6 ]
then
  echo 27 > /sys/class/gpio/export
  sleep 1 ;
fi

# Set to output
echo "out" > /sys/class/gpio/gpio27/direction

# Set to high value
echo 1 > /sys/class/gpio/gpio27/value
