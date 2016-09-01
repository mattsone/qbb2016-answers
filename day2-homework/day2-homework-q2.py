#!/usr/bin/env python
"""
Instructions:  give python file, mapping file, and c tab file separated by spaces, along with arg1,
which if it is any character other than a, will skip non-matching lines.  If a is used for arg1
first column will be replaced by *****

"""
import sys



def ident_map(mapping_file, c_tab, arg1):
    mapping_dict = {}
    for line in open(mapping_file):
        fields = line.rstrip("\r\n").split("\t")
        Swiss_prot = fields[0]
        flybase_AC = fields[-1]
        mapping_dict[flybase_AC] = Swiss_prot
        
    for i, line in enumerate(open(c_tab)):
        if i == 0:
            continue
        fields2 = line.rstrip("\r\n").split("\t")
        gene_name = fields2[8]
        if gene_name in mapping_dict:
            print mapping_dict[gene_name], "\t" , line
        if gene_name not in mapping_dict and arg1 == "a":
           
            fields2[1] = "***********"
            print fields2[1], "\t" , line
                
            
            
            
            
ident_map(sys.argv[1], sys.argv[2], sys.argv[3])




        
    