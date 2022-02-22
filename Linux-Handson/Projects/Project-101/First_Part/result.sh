#!/bin/bash

echo -e "Bu script *nightfighter* AWS-DevOps Grubu tarafindan yapilmiştir.\n"
#Validate if file is given
if [[ ! -f $1  ]]
then
        echo "please type a file"
        exit
fi
#Method #1
cat $1 | grep serdar | grep Terminate | grep -Eo "i-[a-zA-Z0-9]{17}" | sort -u > result.txt

#Method #2
cut -d " "  -f 1,4,9  $1 | grep -Fiw serdar | grep -Fiw terminateinstances | awk '{split($0,a,","); print a[10]}' | awk '{split($0,a,":");print a[2]}' | tr -d '}]"' |sort | uniq > result.txt

#Method #3
cat $1 | grep -i "serdar" | grep -i "terminateinstance"  | awk -F'"' '{print $16}' | cat >> result.txt

cat $1 | grep -i "serdar" | grep -i "terminateinstance"  | awk -F'"' '{print $32}' | cat >> result.txt

cat $1 | grep -i "serdar" | grep -i "terminateinstance"  | awk -F'"' '{print $48}' | cat >> result.txt

cat $1 | grep -i "serdar" | grep -i "terminateinstance"  | awk -F'"' '{print $64}' | cat >> result.txt

cat $1 | grep -i "serdar" | grep -i "terminateinstance"  | awk -F'"' '{print $80}' | cat >> result.txt

cat $1 | grep -i "serdar" | grep -i "terminateinstance"  | awk -F'"' '{print $96}' | cat >> result.txt

sort result.txt | uniq | tee result1.txt