'''
Given the head of a singly linked list, your task is to left rotate the linked list k times.

Examples:

Input: head = 10 -> 20 -> 30 -> 40 -> 50, k = 4
Output: 50 -> 10 -> 20 -> 30 -> 40
Explanation:
Rotate 1: 20 -> 30 -> 40 -> 50 -> 10
Rotate 2: 30 -> 40 -> 50 -> 10 -> 20
Rotate 3: 40 -> 50 -> 10 -> 20 -> 30
Rotate 4: 50 -> 10 -> 20 -> 30 -> 40

Input: head = 10 -> 20 -> 30 -> 40 , k = 6
Output: 30 -> 40 -> 10 -> 20 
 
Constraints:

1 <= number of nodes <= 105
0 <= k <= 109
0 <= data of node <= 109
'''

class Solution:
    def rotate(self, head, k):
        if k == 0 or head is None:
            return head
        current = head
        length = 1
        
        while current.next is not None:
            current = current.next
            length += 1
        k %= length
        
        if k == 0:
            current.next = None
            return head
        current.next = head
        current = head
        
        for _ in range(1, k):
            current = current.next
        newHead = current.next
        
        current.next = None
        return newHead