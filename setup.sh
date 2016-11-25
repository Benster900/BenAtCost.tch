#!/bin/bash

yum install git -y
yum install python-pip python-devel gcc nginx -y
source env/bin/activate
pip install -r requirements.txt
cp benatcost.service /etc/systemd/system/
sudo chown nginx:nginx -R ../BenAtCost.tech
