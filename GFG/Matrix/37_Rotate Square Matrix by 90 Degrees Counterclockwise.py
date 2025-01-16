'''
Given a n*n square matrix mat[][], rotate it by 90 degrees in counterclockwise direction without using any extra space.

Examples: 

Input: mat[][] = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
Output: [[3, 6, 9], 
                [2, 5, 8], 
                [1, 4, 7]]

Input: mat[][] = [[1, 2,  3, 4],
            [5, 6, 7,  8], 
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
Output: [[4, 8, 12, 16], 
              [3, 7, 11, 15],
              [2, 6, 10, 14],
              [1, 5, 9, 13]]
'''

# python3 program to rotate a matrix by 90 degrees anti-
# clockwise by reversing Rows and then Transposing
def rotateMatrix(mat):
    n = len(mat)
    
    # Reverse each row
    for row in mat:
        row.reverse()

    # Performing Transpose
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

if __name__ == "__main__":
    mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]

    rotateMatrix(mat)

    # Print the rotated matrix
    for row in mat:
      print(" ".join(map(str, row)))