'''
Given a matrix mat[][] and an integer x, the task is to check if x is present in mat[][] or not. Every row and column of the matrix is sorted in increasing order.

Examples: 

Input: x = 62, mat[][] = [[3, 30, 38],
[20, 52, 54],
[35, 60, 69]]
Output: false
Explanation: 62 is not present in the matrix.

Input: x = 55, mat[][] = [[18, 21, 27],
[38, 55, 67]]
Output: true
Explanation: mat[1][1] is equal to 55.

Input: x = 35, mat[][] = [[3, 30, 38],
[20, 52, 54],
[35, 60, 69]]
Output: true
Explanation: mat[2][0] is equal to 35.
'''

# Python program to search an element in row-wise
# and column-wise sorted matrix

def matSearch(mat, x):
    n = len(mat)
    m = len(mat[0])
    i = 0
    j = m - 1

    while i < n and j >= 0:
      
        # If x > mat[i][j], then x will be greater
        # than all elements to the left of 
        # mat[i][j] in row i, so increment i
        if x > mat[i][j]:
            i += 1
      
        # If x < mat[i][j], then x will be smaller
        # than all elements to the bottom of
        # mat[i][j] in column j, so decrement j
        elif x < mat[i][j]:
            j -= 1
      
        # If x = mat[i][j], return true
        else:
            return True

    # If x was not found, return false
    return False

if __name__ == "__main__":
    mat = [
        [3, 30, 38],
        [20, 52, 54],
        [35, 60, 69]
    ]
    x = 35
    if matSearch(mat, x):
        print("true")
    else:
        print("false")