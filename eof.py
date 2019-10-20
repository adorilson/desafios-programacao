#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

for line in sys.stdin:
    # x is the line without \n
    x = line.split("\n")[0]
    # do the magic here
    print(x)
    
print("exit")
