# -*- coding: utf-8 -*-
"""
Advent of Code - Day 01

@author: Diogo Barros
"""

import re

values=[]

with open("input.txt",'r') as text:
    for line in text:
        #Saving all int matches in a temp array
        matches=re.findall(r'\d',line)
        first = matches[0]
        last = matches[-1]
        #append the 2 digit number to the 'values' array
        values.append(int(first+last))
        
print("Sum of all calibration values is: " + str(sum(values)))        
     


