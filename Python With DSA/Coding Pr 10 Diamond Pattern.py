def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    # Initialize an empty list
    diamond = []
    
    # upper part of the diamond + middle row
    for i in range(1, n + 1):
        
        # stars = 2 * i - 1
        stars = '*' * (2 * i - 1)
        
        # leading spaces = n - i
        spaces = ' ' * (n - i)
        
        diamond.append(spaces + stars + spaces)
    
    # lower part
    
    for i in range(n - 1, 0, -1):
    
        # Number of stars in the current row is 2 * i - 1
        stars = '*' * (2 * i - 1)
        # Number of leading spaces to center the stars is n - i
        spaces = ' ' * (n - i)
        # Add the centered row to the list
        diamond.append(spaces + stars + spaces)
    
    # Return the list of diamond rows
    return diamond

n = 5
diamond = generate_diamond(n)
for row in diamond:
    print(row)