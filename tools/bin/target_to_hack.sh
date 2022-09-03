#!/bin/sh

target=$(cat ~/.config/bin/target)

if [ -n "$target" ]; then
    echo "%{F#FFAF60} ﲅ%{F#ffffff} $target %{u-}"
else
    echo "%{u-} %{F#A44BA0}ﲅ%{F#ffffff} No target "
fi
