#!/bin/sh

target=$(cat ~/.config/bin/target)

if [ -n "$target" ]; then
    echo "%{F#CFC77C} 什%{F#ffffff} $target %{u-}"
else
    echo "%{u-} %{F#808080}什%{F#808080} No target "
fi
