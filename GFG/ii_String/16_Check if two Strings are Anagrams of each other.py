'''
Given two strings s1 and s2 consisting of lowercase characters, the task is to check whether the two given strings are anagrams of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different.

Examples:

Input: s1 = “geeks”  s2 = “kseeg”
Output: true
Explanation: Both the string have same characters with same frequency. So, they are anagrams.

Input: s1 = “allergy”  s2 = “allergic”
Output: false
Explanation: Characters in both the strings are not same. s1 has extra character 'y' and s2 has extra characters 'i' and 'c', so they are not anagrams.

Input: s1 = "g", s2 = "g"
Output: true
Explanation: Characters in both the strings are same, so they are anagrams.
'''

# Python Code to check if two Strings are anagram of 
# each other using Dictionary

def areAnagrams(s1, s2):
    
    # Create a hashmap to store character frequencies
    charCount = {}
    
    # Count frequency of each character in string s1
    for ch in s1:
        charCount[ch] = charCount.get(ch, 0) + 1
  
    # Count frequency of each character in string s2
    for ch in s2:
        charCount[ch] = charCount.get(ch, 0) - 1
  
    # Check if all frequencies are zero
    for value in charCount.values():
        if value != 0:
            return False
    
    # If all conditions satisfied, they are anagrams
    return True

if __name__ == "__main__":
    s1 = "geeks"
    s2 = "kseeg"
    print("true" if areAnagrams(s1, s2) else "false")