'''
Add Number Linked Lists
Given the head of two singly linked lists num1 and num2 representing two non-negative integers. The task is to return the head of the linked list representing the sum of these two numbers.
For example, num1 represented by the linked list : 1 -> 9 -> 0, similarly num2 represented by the linked list: 2 -> 5. Sum of these two numbers is represented by 2 -> 1 -> 5.

Note: There can be leading zeros in the input lists, but there should not be any leading zeros in the output list.

Examples:

Input: num1 = 4 - > 5, num2 = 3 -> 4 -> 5
Output:  3 -> 9 -> 0
 
Explanation: Given numbers are 45 and 345. There sum is 390.
Input: num1 = 0 -> 0 -> 6 -> 3, num2 = 0 -> 7 
Output: 7 -> 0 
 
Explanation: Given numbers are 63 and 7. There sum is 70.
Constraints:
1 <= size of both linked lists <= 106
0 <= elements of both linked lists <= 9
'''

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def reverseList(self, head):        
        curr = head
        prev = None
        while curr!= None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
            
            
    
    def addTwoLists(self, num1, num2):

        head1 = num1
        head2 = num2
        
        curr1 = self.reverseList(num1)
        curr2 = self.reverseList(num2)
        
        rem = 0
        head3 = None
        curr3 = None
        while curr1!=None and curr2!=None:
            
            data = curr1.data + curr2.data + rem
            value = data%10
            rem = data//10
            
            new_node = Node(value)
            if head3==None:
                head3 = new_node
                curr3 = head3
            else:
                curr3.next = new_node
                curr3 = curr3.next
            
            
            curr1 = curr1.next
            curr2 = curr2.next
        
        if curr1 == None and curr2 == None and rem !=0:
            new_node = Node(rem)
            curr3.next = new_node
            curr3 = curr3.next
            
        while curr1!=None:
            data = curr1.data + rem
            value = data%10
            rem = data//10
            
            new_node = Node(value)
            curr3.next = new_node
            curr3 = curr3.next
            
            curr1 = curr1.next
        
        
        while curr2!=None:
            data = curr2.data + rem
            value = data%10
            rem = data//10
            
            new_node = Node(value)
            curr3.next = new_node
            curr3 = curr3.next
            
            curr2 = curr2.next
            
        curr3.next = None
        
        head = self.reverseList(head3)
        
        new_curr = head
        
        while new_curr!= None:
            if new_curr.data!=0:
                return new_curr
            
            new_curr = new_curr.next