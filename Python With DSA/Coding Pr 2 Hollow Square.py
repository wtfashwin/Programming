def hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    
    # Initialize an empty list to store the rows of the hollow square
    square = []
    
    # Handle the case when n is 1 separately
    if n == 1:
        return ['*']
    
    # The first and last rows are full of '*'
    square.append('*' * n)  # First row
    
    # For the middle rows, the first and last characters are '*', rest are spaces
    for i in range(n - 2):
        square.append('*' + ' ' * (n - 2) + '*')
    
    # The last row is also full of '*'
    square.append('*' * n)  # Last row
    
    k# Return the list of rows
    return square

# Example usage
n = 5
square = hollow_square(n)
for row in square:
  print(row)