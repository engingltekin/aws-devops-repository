#!/bin/bash

#Method #1
echo -e $(cat certificate.pem) | tee new.pem

#Method #2
sed 's/\\n/\n/g' certificate.pem | tee new1.pem
