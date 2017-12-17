#!/usr/bin/env python
# encoding: utf-8

HOST = 'localhost'
with open('/home/ec2-user/SQLConfig.conf', 'r') as myfile:
    HOST=myfile.read().replace('\n', '')
