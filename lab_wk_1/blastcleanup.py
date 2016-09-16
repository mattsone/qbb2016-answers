#!/usr/bin/env python

import sys

file1 = open(sys.argv[1])

for line in file1:
    #line.translate(None, '-')
    fields = line.rstrip("\r\n").split("\t")
    length = int(fields[2]) - int(fields[1])
    length = int(length)
    if length == 10292:
        print ">" + fields[0] + "\n" + fields[3].translate(None, '-') + "\r\n"
        
        
    
    