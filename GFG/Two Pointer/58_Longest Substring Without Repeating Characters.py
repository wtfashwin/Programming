'''
Given a string s having lowercase characters, find the length of the longest substring without repeating characters. 

Examples:

Input: s = "geeksforgeeks"
Output: 7
Explanation: The longest substrings without repeating characters are "eksforg” and "ksforge", with lengths of 7.

Input: s = "aaa"
Output: 1
Explanation: The longest substring without repeating characters is "a"

Input: s = "abcdefabcbb"
Output: 6
Explanation: The longest substring without repeating characters is "abcdef".
'''

# Python code to find the largest substring with non-repeating
# characters using last index of repeated character

MAX_CHAR = 26

def longestUniqueSubstr(s):
    n = len(s)
    res = 0

    # last index of all characters is initialized as -1
    lastIndex = [-1] * MAX_CHAR

    # Initialize start of current window
    start = 0

    # Move end of current window
    for end in range(n):

        # Find the last index of s[end]
        # Update starting index of current window as
        # maximum of current value of end and last index + 1
        start = max(start, lastIndex[ord(s[end]) - ord('a')] + 1)

        # Update result if we get a larger window
        res = max(res, end - start + 1)

        # Update last index of s[end]
        lastIndex[ord(s[end]) - ord('a')] = end

    return res

if __name__ == "__main__":
    s = "geeksforgeeks"
    print(longestUniqueSubstr(s))