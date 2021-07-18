#!/bin/bash



PROGRAM="conky"

if pgrep -x "$PROGRAM" >/dev/null
then
	echo "$PROGRAM is running"
	killall conky
	sleep 1
	conky -c ~/.config/conky/conky2i3rc
	conky -c ~/.config/conky/conkyi3rc

else
	echo "$PROGRAM is not running"
	sleep 1
	conky -c ~/.config/conky/conky2i3rc
	conky -c ~/.config/conky/conkyi3rc
fi
