#!/bin/bash
. ~/.bashrc
RAINY_PATH=$rainy_path 
URL="\"$RAINY_PATH\""


# Cloudy wallpaper
the_script='tell application "System Events" to tell every desktop to set picture to '
osascript -e "${the_script}${URL}"