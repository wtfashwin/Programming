'''
Given a string s of lowercase English letters, the task is to find the first non-repeating character. If there is no such character, return '$'.

Examples: 

Input: s = "geeksforgeeks"
Output: 'f'
Explanation: 'f' is the first character in the string which does not repeat.

Input: s = "racecar"
Output: 'e'
Explanation: 'e' is the only character in the string which does not repeat.

Input: "aabbccc"
Output: '$'
Explanation: All the characters in the given string are repeating.
'''

# Python program to find the index

# As the input string can only have lowercase 
# characters, the maximum characters will be 26
MAX_CHAR = 26

def nonRepeatingChar(s):
  
    # Initialize frequency array
    freq = [0] * MAX_CHAR

    # Count the frequency of all characters
    for c in s:
        freq[ord(c) - ord('a')] += 1

    # Find the first character with frequency 1
    for i in range(len(s)):
        if freq[ord(s[i]) - ord('a')] == 1:
            return s[i]
    
    # If no character with a frequency of 1 is 
    # found, then return '$'
    return '$'

s = "racecar"
  
print(nonRepeatingChar(s))