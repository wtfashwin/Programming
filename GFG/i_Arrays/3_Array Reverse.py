'''Given an array arr[], the task is to reverse the array. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.

Examples:

Input: arr[] = {1, 4, 3, 2, 6, 5}
Output: {5, 6, 2, 3, 4, 1}
Explanation: The first element 1 moves to last position, the second element 4 moves to second-last and so on.

Input: arr[] = {4, 5, 1, 2}
Output: {2, 1, 5, 4}
Explanation: The first element 4 moves to last position, the second element 5 moves to second last and so on.

Using Two Pointers - O(n) Time and O(1) Space
The idea is to maintain two pointers: 
left and right, such that left points at the beginning of the array and right 
points to the end of the array.

While left pointer is less than the right pointer, swap the elements at these 
two positions. After each swap, increment the left pointer and decrement the 
right pointer to move towards the center of array. This will swap all the elements 
in the first half with their corresponding element in the second half.
'''
# Python Program to reverse an array using Two Pointers

# function to reverse an array
def reverseArray(arr):
    
    # Initialize left to the beginning and right to the end
    left = 0
    right = len(arr) - 1
  
    # Iterate till left is less than right
    while left < right:
        
        # Swap the elements at left and right position
        arr[left], arr[right] = arr[right], arr[left]
      
        # Increment the left p
        # ointer
        left += 1
      
        # Decrement the right pointer
        right -= 1

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]

    reverseArray(arr)
  
    for i in range(len(arr)):
        print(arr[i], end=" ")