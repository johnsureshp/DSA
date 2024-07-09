# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:08:12 2024

@author: P.JOHN
"""

def binary(arr,target):
    left =0
    right =len(arr)-1
    while left<=right:
        mid =(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]< target:
            left =mid+1
        else:
            right = mid-1
arr = [ 2, 3, 7, 7, 11, 15, 25]

print(binary(arr, 15))