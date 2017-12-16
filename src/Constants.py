#!/usr/bin/env python
# encoding: utf-8

HOST = 'localhost'
with open('../../SQLConfig.conf', 'r') as myfile:
    HOST=myfile.read().replace('\n', '')
