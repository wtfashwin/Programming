'''
Inverted Right Angled Triangle
Problem Description:

You are given an integer n. Your task is to return an inverted right-angled triangle pattern of '*' where each side has n characters, represented as a list of strings. The first row should have n stars, the second row n-1 stars, and so on, until the last row has 1 star.



Input Parameters:

n (int): The height and base of the inverted right-angled triangle.


Output:

A list of strings where each string is a row of '*' characters that decreases in length from n to 1.



Example:

Input: 3
Output: ['***', '**', '*']
***
**
*
 
Input: 5
Output: ['*****', '****', '***', '**', '*']

*****
****
***
**
*
'''

def generate_triangle(n):
    """ function returns an inverted right angled triangle"""
    tri = [] # list to store 

    for i in range(n, 0 , -1): # for loop (start = n , stop= 0 , step = -1)
    
        tri.append("*" * i) # append * in list
    return tri
