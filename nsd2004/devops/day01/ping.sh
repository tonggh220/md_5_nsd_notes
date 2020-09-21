#!/bin/bash

for ip in 192.168.1.{1..254}
do
  ping -c2 $ip &> /dev/null && echo "$ip:up" || echo "$ip:down" &
done
