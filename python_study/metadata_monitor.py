#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

filename = '/Users/gengmei/PycharmProjects/python_study/1_input_print.py'
command = subprocess.getoutput(('cat ' + filename + " | grep -i 'print'").lower())
print(command)
if 'print' in command:
    print('============')

os.system(command)