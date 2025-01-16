'''
Given a matrix mat[][] of size nxm, the task is to update the matrix such that if an element is zero, set its entire row and column to zeroes.

Examples:

Input: mat[][] = [[1, -1, 1],
[-1, 0, 1],
[1, -1, 1]]
Output: [[1, 0, 1],
[0, 0, 0],
[1, 0, 1]]
Explanation: mat[1][1] = 0, so all elements in row 1 and column 1 are updated to zeroes.

Input: mat[][] = [[0, 1, 2, 0],
[3, 4, 0, 2],
[1, 3, 1, 5]]
Output: [[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 3, 0, 0]]
Explanation: mat[0][0], mat[1][2] and mat[0][3] are 0s, so all elements in row 0, row 1, column 0, column 2 and column 3 are updated to zeroes.
'''

# Python code to implement Set Matrix Zeroes using
# first row and column

def setMatrixZeroes(mat):
    n = len(mat)
    m = len(mat[0])

    c0 = 1

    # Traverse the arr and mark first cell of each row and column
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:

                # mark i-th row
                mat[i][0] = 0

                # mark j-th column
                if j == 0:
                    c0 = 0
                else:
                    mat[0][j] = 0

    # Traverse and mark the matrix from (1, 1) to (n - 1, m - 1)
    for i in range(1, n):
        for j in range(1, m):

            # Check for col & row
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0

    # Mark the first row
    if mat[0][0] == 0:
        for j in range(m):
            mat[0][j] = 0

    # Mark the first column
    if c0 == 0:
        for i in range(n):
            mat[i][0] = 0
            

if __name__ == "__main__":
    mat = [
        [0, 1, 2, 0],
        [3, 4, 0, 2],
        [1, 3, 1, 5]
    ]

    setMatrixZeroes(mat)

    for row in mat:
        print(" ".join(map(str, row)))