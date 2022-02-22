#!/bin/bash

sed -i "s/ec2-private_ip/$(cat info.json | grep -i PrivateIpAddress | head -1 | cut -d'"' -f 4)/"      terraform.tf
#sed -i "s/ec2-private_ip/$(cat info.json | grep PrivateIpAddress | cut -d'"' -f4 | sort -u | sed '1d')/ig" terraform.tf
