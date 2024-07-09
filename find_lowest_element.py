# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:52:11 2024

@author: P.JOHN
"""
def lowest_element(my_array):
    mini = my_array[0]
    for i in range(1,len(my_array)):
        if my_array[i]< mini:
            mini =my_array[i]
    return mini

my_array = [7, 12, 9, 4, 11]
print(lowest_element(my_array))