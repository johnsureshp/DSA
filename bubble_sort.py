# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:23:22 2024

@author: P.JOHN
"""
arr = [ 2, 3, 7, 7, 11, 15, 25]
def bubble_sort(arr):
        
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

               
print(bubble_sort(arr))