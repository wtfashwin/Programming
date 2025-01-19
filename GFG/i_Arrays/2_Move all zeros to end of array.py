'''Given an array of integers arr[], the task is to move all the zeros to the end of the array while maintaining the relative order of all non-zero elements.

Examples: 

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: arr[] = [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.

Input: arr[] = [10, 20, 30]
Output: arr[] = [10, 20, 30]
Explanation: No change in array as there are no 0s.

Input: arr[] = [0, 0]
Output: arr[] = [0, 0]
Explanation: No change in array as there are all 0s.'''

#The idea is similar to the previous approach where we took a pointer, 
# say count to track where the next non-zero element should be placed. 
# However, on encountering a non-zero element, instead of directly 
# placing the non-zero element at arr[count], we will swap the non-zero 
# element with arr[count]. This will ensure that if there is any zero 
# present at arr[count], it is pushed towards the end of array and is not overwritten.


# Python Program to move all zeros to end using one traversal

# Function which pushes all zeros to end of array
def pushZerosToEnd(arr):
    
    # Pointer to track the position for next non-zero element
    count = 0
    
    for i in range(len(arr)):
        
        # If the current element is non-zero
        if arr[i] != 0:
            
            # Swap the current element with the 0 at index 'count'
            arr[i], arr[count] = arr[count], arr[i]
            
            # Move 'count' pointer to the next position
            count += 1

if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)
    for num in arr:
        print(num, end=" ")