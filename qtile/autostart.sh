#!/bin/bash

#udiskie &
nitrogen --restore &
picom --config /home/naepho/.config/qtile/picom.conf &
bash /home/naepho/.config/qtile/x11.sh &
cd /home/naepho
