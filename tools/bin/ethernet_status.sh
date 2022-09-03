#!/bin/sh

ETH=$(/usr/sbin/ifconfig wlp3s0 | grep 'inet ' | awk '{print $2}')

if [ -z "$ETH" ]
then
  #echo "%{F#ffffff}%{u-} Internet Off "
  echo "%{u-}%{F#A44BA0}  %{F#ffffff}Internet Off "
else
  echo "%{F#2495e7}  %{F#ffffff}$(/usr/sbin/ifconfig wlp3s0 | grep "inet " | awk '{print $2}') %{u-}"
fi
