#!/bin/bash
. ~/.bashrc
CLEAR_PATH=$clear_path 
URL="\"$CLEAR_PATH\""


# Cloudy wallpaper
the_script='tell application "System Events" to tell every desktop to set picture to '
osascript -e "${the_script}${URL}"
