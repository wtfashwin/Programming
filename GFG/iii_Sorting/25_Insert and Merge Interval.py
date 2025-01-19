'''
Given a set of non-overlapping intervals and a new interval, the task is to insert the interval at the correct position such that after insertion, the intervals remain sorted. If the insertion results in overlapping intervals, then merge the overlapping intervals. Assume that the set of non-overlapping intervals is sorted based on start time.

Examples: 

Input: intervals[][] = [[1, 3], [4, 5], [6, 7], [8, 10]], newInterval[] = [5, 6]
Output: [[1, 3], [4, 7], [8, 10]]
Explanation: The intervals [4, 5] and [6, 7] are overlapping with [5, 6]. So, they are merged into one interval [4, 7].

Input: intervals[][] = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval[] = [4, 9]
Output: [[1, 2], [3, 10], [12, 16]]
Explanation: The intervals [ [3, 5], [6, 7], [8, 10] ] are overlapping with [4, 9]. So, they are merged into one interval [3, 10].
'''

'''
When we add a new interval, it may overlap with some contiguous intervals in the array. The overlapping intervals can be found in a contiguous subarray because the intervals array is already sorted. To remove overlapping we find these overlapping interval's subarray and merge them with new interval, to form a single merged interval.

Now to maintain the order sorted, we first add the lower intervals, then this merged interval, and finally the remaining intervals in the result.
'''

# Function
def insertInterval(intervals, newInterval):
    res = []
    i = 0
    n = len(intervals)

    # Add all intervals that come before the new interval
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1

    # Merge all overlapping intervals with the new interval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
        
    res.append(newInterval)

    # Add all the remaining intervals
    while i < n:
        res.append(intervals[i])
        i += 1

    return res

if __name__ == "__main__":
    intervals =  [[1, 3], [4, 5], [6, 7], [8, 10]]
    newInterval = [5, 6]

    res = insertInterval(intervals, newInterval)
    for interval in res:
        print(interval[0], interval[1])