'''


You are given a special linked list with n nodes where each node 
has two pointers a next pointer that points to the next node of 
the singly linked list, and a random pointer that points to the 
random node of the linked list.

Construct a copy of this linked list. The copy should consist of 
the same number of new nodes, where each new node has the value 
corresponding to its original node. Both the next and random 
pointer of the new nodes should point to new nodes in the copied 
list, such that it also represent the same list state. None of the 
pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

NOTE : Original linked list should remain unchanged.

Examples:

Input: head = [[1, 3], [3, 3], [5, NULL], [9, 3]] 
      
Output: head = [[1, 3], [3, 3], [5, NULL], [9, 3]] 
Explanation: 
Node 1 points to Node 2 as its NEXT and Node 3 as its RANDOM.
Node 2 points to Node 3 as its NEXT and Node 3 as its RANDOM.
Node 3 points to Node 4 as its NEXT and NULL as its RANDOM.
Node 4 points to NULL as its NEXT and Node 3 as its RANDOM.
Input: head = [[1, 3], [2, 1], [3, 5], [4, 3], [5, 2]]
  
 
Output: head = [[1, 3], [2, 1], [3, 5], [4, 3], [5, 2]]
Explanation: 
Node 1 points to Node 2 as its NEXT and Node 3 as its RANDOM.
Node 2 points to Node 3 as its NEXT and Node 1 as its RANDOM.
Node 3 points to Node 4 as its NEXT and Node 5 as its RANDOM.
Node 4 points to Node 5 as its NEXT and Node 3 as its RANDOM.
Node 5 points to NULL as its NEXT and Node 2 as its RANDOM.
Input: head = [[7, NULL], [7, NULL]]
Output: head = [[7, NULL], [7, NULL]]
Explanation: 
Node 1 points to Node 2 as its NEXT and NULL as its RANDOM.
Node 2 points to NULL as its NEXT and NULL as its RANDOM.

Constraints:
1 <= n <= 100
0 <= node->data <= 1000
'''
# Link list Node
# class Node:

#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.random = None
        
class Solution:
    def cloneLinkedList(self, head):
        # code here
        if not head:
            return None
        
        curr = head
        while curr:
            nn =Node(curr.data)
            nn.next = curr.next
            curr.next = nn
            curr = nn.next
        
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        curr = head
        clhead = head.next
        cl = clhead
        
        while cl.next:
            curr.next = curr.next.next
            cl.next = cl.next.next
            curr = curr.next
            cl = cl.next
        curr.next = None
        cl.next = None
        
        return clhead


class Node:

    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None


def print_linked_list(root):
    link = {}
    temp = root
    index = 0
    while temp:
        link[temp] = index
        temp = temp.next
        index += 1

    temp = root
    result = []
    while temp:
        random_index = "NULL" if not temp.random else link.get(temp.random) + 1
        result.append(f"[{temp.data}, {random_index}]")
        temp = temp.next

    print(f"[{', '.join(result)}]")


def build_linked_list(v, org_address):
    address = [None] * len(v)
    head = Node(v[0][0])
    address[0] = head
    org_address[head] = 0
    temp = head

    for i in range(1, len(v)):
        new_node = Node(v[i][0])
        org_address[new_node] = i
        address[i] = new_node
        temp.next = new_node
        temp = temp.next

    temp = head
    for i in range(len(v)):
        random_index = v[i][1]
        if random_index != -1:
            temp.random = address[random_index - 1]
        temp = temp.next

    return head


def validate_input(org_address, head, v):
    address = [None] * len(v)
    temp = head
    for i in range(len(v)):
        if temp not in org_address or org_address[temp] != i:
            return False
        address[i] = temp
        temp = temp.next

    if temp is not None:
        return False

    temp = head
    for i in range(len(v)):
        value = v[i][0]
        random_index = v[i][1]

        if random_index == -1:
            if temp.random is not None:
                return False
        else:
            temp_node = address[random_index - 1]
            if temp.random != temp_node:
                return False
        temp = temp.next
    return True


def validation(res, org_address):
    temp = res
    while temp:
        if temp in org_address:
            return False
        if temp.random in org_address:
            return False
        temp = temp.next
    return True


def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        v = []
        for _ in range(n):
            a, b = input().split()
            a = int(a)
            b = -1 if b in ["NULL", "N", "null", "n", "Null"] else int(b)
            v.append((a, b))

        org_address = {}
        head = build_linked_list(v, org_address)

        solution = Solution()
        res = solution.cloneLinkedList(head)

        # Validate if input is modified
        if validate_input(org_address, head, v):
            if validation(res, org_address):
                print_linked_list(res)
            else:
                print("Pointing to the original list")
        else:
            print("Input list modified")
        print("~")


if __name__ == "__main__":
    main()