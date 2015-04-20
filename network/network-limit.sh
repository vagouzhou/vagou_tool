#!/bin/sh
ipfw delete 1
bw=$1
ipfw pipe 1 config bw ${bw}Kbits/s  
ipfw add 1 pipe 1 ip from me to 173.37.44.179
