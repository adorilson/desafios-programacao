#!/usr/bin/python
# Read inputs from Standard Input.
# Write outputs to Standard Output.
# Please, do not use fileinput module to read Standard Input.

import sys

n = int(raw_input())
if n==0:
    print 0
else:
    n = raw_input()
    n = n.split()
    closer = int(n[0])
    for i in n:
        if abs(int(i))<abs(closer):
            closer = int(i)
        elif (abs(int(i))==abs(closer) and int(i)>0):
            closer = int(i)
        
    print closer
