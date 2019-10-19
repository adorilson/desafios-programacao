#!/usr/bin/python
# Read inputs from Standard Input.
# Write outputs to Standard Output.
# Please, do not use fileinput module to read Standard Input.

import sys

n = raw_input().split()
n1 = int(n[0])
n2 = int(n[1])

s = raw_input()

words = raw_input().split()
w1 = words[0]
w2 = words[1]

if n1+n2==len(s):
    print w1
else:
    print w2
