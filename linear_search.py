# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:58:47 2024

@author: P.JOHN
"""

def linear_search(arr,target):
    for i in arr:
        if i==target:
            return i
        
arr = [3, 7, 2, 9, 5]
print(linear_search(arr, 21))
    
    