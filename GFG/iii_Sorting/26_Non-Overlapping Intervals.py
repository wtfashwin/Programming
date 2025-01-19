'''
Given a list of intervals with starting and ending values, the task is to find the minimum number of intervals that are required to be removed to make remaining intervals non-overlapping.

Examples:

Input: intervals[][] = [[1, 2], [2, 3], [3, 4], [1, 3]]
Output: 1
Explanation: Removal of [1, 3] makes the ranges non-overlapping.

Input: intervals[][] = [[1, 3], [1, 3], [1, 3]]
Output: 2
Explanation: Removal of two occurrences of [1, 3] makes the remaining ranges non-overlapping.

Input: intervals[][] = [[1, 2], [5, 10], [18, 35], [40, 45]]
Output: 0
Explanation: All ranges are already non-overlapping.
'''

# Python program to minimum number of intervals required
# to be removed to make remaining intervals non-overlapping
# Using sorting by starting value

def minRemoval(intervals):
    cnt = 0

    # Sort by minimum starting point
    intervals.sort(key=lambda x: x[0])

    end = intervals[0][1]
    for i in range(1, len(intervals)):

        # If the current starting point is less than
        # the previous interval's ending point
        # (ie. there is an overlap)
        if intervals[i][0] < end:
          
            # Increase cnt and remove the interval
            # with the higher ending point
            cnt += 1
            end = min(intervals[i][1], end)

        # Incase of no overlapping, this interval is 
        # not removed and 'end' will be updated
        else:
            end = intervals[i][1]

    return cnt

if __name__ == "__main__":
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(minRemoval(intervals))