# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:39:22 2024

@author: student
"""

with open(r"C:\Users\student\Downloads\ict.txt",'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)