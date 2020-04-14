# OSC-Timer
Python timer that takes OSC messages as commands

## Description
The goal of this project is to create a timer in python that runs full screen on a RaspberryPi and can receive OSC messages to start, stop, and add time.

## Outline Of Goals
### Setup Pi
This is mostly complete. I have tested that python and tkinter are working. The only improvement would be to reduce to OS, as this Pi does not need any desktop environment. However, I couldn't initially get tkinter to work without the desktop environment, but I think this was because the X server needs to be installed at least for tkinter to work. Ideally the timer application would start immediately once the Pi is powered on to avoid needing to interface with ssh or keyboard/mouse. 

### Setup Clock
There ideally would be different fonts and layouts (hh:mm:ss or mm:ss) to choose from.

### Setup OSC
The OSC messages will tell the timer to start/stop and add time to the clock. Once different fronts and layouts are available, those will be selectable via OSC as well.

## Roadmap
Verify incoming OSC messages
Create Timer
Define OSC Dictionary for timer
Optimize Debian image size (remove unneccisary stuff)

