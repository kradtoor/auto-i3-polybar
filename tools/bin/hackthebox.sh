#!/bin/sh
 
IFACE=$(/usr/sbin/ifconfig | grep tun0 | awk '{print $1}' | tr -d ':')
 
if [ "$IFACE" = "tun0" ]; then
    echo "%{F#77BD8B}  %{F#ffffff}$(/usr/sbin/ifconfig tun0 | grep "inet " | awk '{print $2}') %{u-}"
else
    echo "%{u-} %{F#A44BA0}%{F#ffffff} VPN Off "
fi
