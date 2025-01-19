'''Given two string s1 and s2 of same length, the task is to check whether s2 is a rotation of s1.

Examples: 

Input: s1 = "abcd", s2 = "cdab"
Output: true
Explanation: After 2 right rotations, s1 will become equal to s2.

Input: s1 = "aab", s2 = "aba"
Output: true
Explanation: After 1 left rotation, s1 will become equal to s2.

Input: s1 = "abcd", s2 = "acbd"
Output: false
Explanation: Strings are not rotations of each other.'''

# Python program to check if two given strings are rotations of each other

# Function to check if s1 and s2 are rotations of each other
def areRotations(s1, s2):
    s1 = s1 + s1

    # find s2 in concatenated string
    return s2 in s1

if __name__ == "__main__":
    s1 = "aab"
    s2 = "aba"

    print("true" if areRotations(s1, s2) else "false")