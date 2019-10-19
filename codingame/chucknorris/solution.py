#!/usr/bin/python
# Read inputs from Standard Input.
# Write outputs to Standard Output.
# Please, do not use fileinput module to read Standard Input.

import sys

def to_blocks(binary):
    blocks = []
    c = binary[0]
    for b in binary[1:]:
        if b==c[0]:
            c = c + b
        else:
            blocks.append(c)
            c=b
    blocks.append(c)
    return blocks


def to_chuck(blocks):
    msg = ''
    for b in blocks:
        if b[0]=='1':
            msg = msg + ' ' + '0 ' + ''.join(['0' for x in xrange(len(b))])
        else:
            msg = msg + ' ' + '00 ' + ''.join(['0' for x in xrange(len(b))])
    return msg.strip()

n = raw_input()

msg = []

binary = ''
for s in n:
    binary = binary + '{0:07b}'.format(ord(s))
    
print to_chuck(to_blocks(binary))

