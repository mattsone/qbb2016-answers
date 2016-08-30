#!/usr/bin/env python

import sys

flybase = {}
for line in sys.stdin:
    if "DROME" in line:
        fields = line.rstrip("\r\n").split()
        Swiss_prot = fields[-2]
        flybase_AC = fields[-1]
        flybase[Swiss_prot] = flybase_AC

for Swiss_prot in flybase:
    print Swiss_prot, "\t\t" ,flybase[Swiss_prot]
    
    
    
    
    
        
        