#!/bin/sh
 
IFACE=$(/usr/sbin/ifconfig | grep tun0 | awk '{print $1}' | tr -d ':')
 
if [ "$IFACE" = "tun0" ]; then
    echo "%{F#B3DD8B}  %{F#ffffff}$(/usr/sbin/ifconfig tun0 | grep "inet " | awk '{print $2}') %{u-}"
else
    echo "%{u-} %{F#808080}%{F#808080} VPN Off "
fi
