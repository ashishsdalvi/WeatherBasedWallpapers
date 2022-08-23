#!/bin/bash
. ~/.bashrc
CLOUDY_PATH=$cloudy_path 
URL="\"$CLOUDY_PATH\""


# Cloudy wallpaper
the_script='tell application "System Events" to tell every desktop to set picture to '
osascript -e "${the_script}${URL}"


