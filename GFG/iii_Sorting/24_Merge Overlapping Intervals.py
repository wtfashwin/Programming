'''
Given an array of time intervals where arr[i] = [starti, endi], the task is to merge all the overlapping intervals into one and output the result which should have only mutually exclusive intervals.

Examples:

Input: arr[] = [[1, 3], [2, 4], [6, 8], [9, 10]]
Output: [[1, 4], [6, 8], [9, 10]]
Explanation: In the given intervals, we have only two overlapping intervals [1, 3] and [2, 4]. Therefore, we will merge these two and return [[1, 4]], [6, 8], [9, 10]].

Input: arr[] = [[7, 8], [1, 5], [2, 4], [4, 6]]
Output: [[1, 6], [7, 8]]
Explanation: We will merge the overlapping intervals [[1, 5], [2, 4], [4, 6]] into a single interval [1, 6].
'''

'''
Sort all intervals in increasing order of start time.
Traverse sorted intervals starting from the first interval, 
Do the following for every interval.
If the current interval is not the first interval and it overlaps with the previous interval, then merge it with the previous interval. Keep doing it while the interval overlaps with the previous one.         
If the current interval does not overlap with the previous interval, move to the next interval.
'''

# Python Code to Merge Overlapping Intervals in-place

# Merge overlapping intervals in-place. We return
# modified size of the array arr.
def mergeOverlap(arr):
    
    # Sort intervals based on start values
    arr.sort()

    # Index of the last merged 
    resIdx = 0

    for i in range(1, len(arr)):
        
        # If current interval overlaps with the 
        # last merged interval
        if arr[resIdx][1] >= arr[i][0]:           
            arr[resIdx][1] = max(arr[resIdx][1], arr[i][1])
        
        # Move to the next interval
        else:            
            resIdx += 1
            arr[resIdx] = arr[i]

    # Returns size of the merged intervals
    return resIdx + 1

if __name__ == "__main__":
    arr = [[7, 8], [1, 5], [2, 4], [4, 6]]
    
    # Get the new size of the array after merging
    newSize = mergeOverlap(arr)

    # Print the merged intervals based on the new size
    for i in range(newSize):
        print(arr[i][0], arr[i][1])