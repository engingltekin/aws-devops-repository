#!/bin/bash


  awk '/serdar/ {print $1 $4 $9}' event_history.csv | awk '/TerminateInstances/' | awk '{split($0,a,","); print a[10]}' | awk '{split($0,a,":");print a[2]}' | tr -d '}]"'> result2.txt
