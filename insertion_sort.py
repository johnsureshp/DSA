# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:44:41 2024

@author: P.JOHN
"""

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(1,n):
    print(f'-----------------------------------------------------------------------')
    print(f"present index {i}")
    insert_index = i
    current_value = my_array.pop(i)
    print(f"current value  {current_value}")
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            print(f"{my_array[j]} > {current_value}")
            
            insert_index = j
            print(f'{insert_index}')

    my_array.insert(insert_index, current_value)
    print(my_array)

print("Sorted array:", my_array)