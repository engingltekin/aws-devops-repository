#!/bin/bash

echo "The names of the invalid users: "
cat auth.log | grep -i invalid | awk '{print $9}' | grep -v "from" | grep -v "invalid" | sort -u
echo "The attack number to our system: "
cat auth.log | grep -i invalid | awk '{print $9}' | grep -v "from" | grep -v "invalid" | wc -l

cat auth.log | grep -i "invalid user " | cut -d' ' -f 8 | sort | uniq >>invalid_user.txt
cat auth.log | grep -i "invalid user " | cut -d' ' -f 9 | sort | uniq >>invalid_user.txt

cat invalid_user.txt | grep -v "from" | grep -v "user" > new_invalid_user.txt
