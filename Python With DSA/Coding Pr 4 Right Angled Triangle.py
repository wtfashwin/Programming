'''
Problem Description:

You are given an integer n. Your task is to return a right-angled triangle pattern of '*' where each side has n characters, represented as a list of strings. The triangle has '*' characters, starting with 1 star in the first row, 2 stars in the second row, and so on until the last row has n stars.


Input Parameters:

n (int): The height and base of the right-angled triangle.

Output:

A list of strings where each string is a row of '*' characters that increases in length from 1 to n.

Example:

Input: 3
Output: ['*', '**', '***']
 
Input: 5
Output: ['*', '**', '***', '****', '*****'] '''


def generate_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Initialize an empty list to store the rows of the triangle
    triangle = []
    
    # Loop through each row from 1 to n
    for i in range(1, n+1):
        # Create a row with i '*' characters and append it to the list
        triangle.append('*' * i)
    
    # Return the list of rows
    return triangle