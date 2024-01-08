# -*- coding: utf-8 -*-
"""
Advent of Code - Day 01 - Part 2

@author: Diogo Barros
"""

import re

values=[]
mydic={'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5',
       'six':'6', 'seven':'7', 'eight':'8','nine':'9'}

with open("input.txt",'r') as text:
    
    for line in text:
        
        #This dictionarty will hold the index of all numbers/worded numbers
        indexes={}
        
        #Finding the index of each 'worded number'. Each word can occur +1 times in each line
        for key in mydic:
            if key in line:
                for word_match in re.finditer(key, line):
                    indexes[word_match.start()]=mydic[key]
        
        #Finding the index of each number. Each number can occur +1 times in each line
        for number_match in re.finditer(r'[1-9]', line):
            indexes[number_match.start()]=number_match[0]
        
        #Selecting the first number
        first = indexes[min(indexes)]
        last = indexes[max(indexes)]
        values.append(int(first+last))
      
print("Sum of all calibration values is: " + str(sum(values)))        
     


