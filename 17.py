# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:33:43 2024

@author: student
"""

import csv
# Reading from a CSV file
with open(r'C:\Users\student\Downloads\data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Subject', 'Mark'])
    writer.writerow(['Aansh', 'PWP', 9])
    writer.writerow(['Ashutosh', 'PWP', 10])
    file.close()