'''
Given a matrix mat[][] of size m x n, the task is to print all elements of the matrix in spiral form.

Examples: 

Input: mat[][] = [[1,   2,   3,   4],
              [5,    6,   7,   8],
              [9,   10,  11,  12],
            [13,  14,  15,  16]]
Output: [ 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10 ]

'''
# Python program to perform spiral order
# traversal of a matrix

def spirallyTraverse(mat):
    m, n = len(mat), len(mat[0])

    # List to store the spiral order elements
    res = []

    # Initialize boundaries
    top, bottom, left, right = 0, m - 1, 0, n - 1

    # Iterate until all elements are printed
    while top <= bottom and left <= right:

        # Print top row from left to right
        for i in range(left, right + 1):
            res.append(mat[top][i])
        top += 1

        # Print right column from top to bottom
        for i in range(top, bottom + 1):
            res.append(mat[i][right])
        right -= 1

        # Print bottom row from right to left (if exists)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(mat[bottom][i])
            bottom -= 1

        # Print left column from bottom to top (if exists)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(mat[i][left])
            left += 1

    return res


if __name__ == "__main__":
    mat = [[1, 2, 3, 4], 
           [5, 6, 7, 8], 
           [9, 10, 11, 12], 
           [13, 14, 15, 16]]

    res = spirallyTraverse(mat)
    print(" ".join(map(str, res)))