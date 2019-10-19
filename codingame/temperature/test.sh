#!/bin/bash
# Run this script to easily test your solution
test=1

# Uncomment these next lines to test other inputs!
# test=2
# test=3

./solution.py < in$test.txt | compare out$test.txt
