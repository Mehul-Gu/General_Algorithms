# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 18:56:06 2022

@author: mgupta
"""
def min(array):
    i = 0
    min = array[i]
    while i+1<len(array):
        i = i+1
        new = array[i]
        if new < min:
            min = new
    return min
    
def GCD_Solver(array):

    check = True
    i = min(input)
    while (check == True) and (i < 2):
        j = 0
        check = False
        while (j < len(array)) and (check == False): 
            if array[j] % i != 0:
                check = True
            j = j+1
        i = i-1
    print(i)
        
if __name__ == '__main__':
    input = [4, 8]
    GCD_Solver(input)