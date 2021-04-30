#!/bin/bash


echo "$(playerctl metadata title | awk -v len=40 '{ if (length($0) > len) print substr($0, 1,     len-3) "..."; else print; }' | tr -d '&' | awk '{print "♫ " $0 ""}')" "-$(playerctl metadata artist)-"
