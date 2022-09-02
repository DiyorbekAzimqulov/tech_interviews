from typing import List, Optional
"""
Question: 

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Solution Conceptual overview:

again we use two pointer technique here. one pointer points to only unique numbers which
does not have any duplicates. And one for iteration. In order to identify whether current 
iteration node to be unique we need to be able to access its previous node, that is why we
also keep track of previous node of the current iteration node. 

Each step in iteration -> check whether current node is unique, if it is, then we link unique 
number pointer to that current unique number.
We used dummy node here to handle edge case which first node might be duplicate.

Complexity analysis:
Time -> O(n)
Space -> O(1)

"""

values = [1,2,3,3,4,4,5]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def make_linked_list(array: list) -> ListNode:
    head = ListNode(array[0])
    cur = head
    for i in range(1, len(array)):
        node = ListNode(array[i])
        cur.next = node
        cur = node
    return head

def make_array(head: ListNode) -> list:
    array = []
    while head is not None:
        array.append(head.val)
        head = head.next
    return array

head = make_linked_list(values)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def is_unique(self, head: ListNode, prev: ListNode) -> bool:
        if prev.val != head.val and head.next is None:
            return True
        if prev.val != head.val and head.next and head.val != head.next.val:
            return True

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head and head.next is None:
            return head
        # dummy head
        dummy_head = ListNode(-101)
        dummy_head.next = head
        prev_unique = dummy_head
        prev = dummy_head
        cur = dummy_head.next
        while cur is not None:
            if prev_unique.val == cur.val:
                prev = cur
                cur = cur.next
            else:
                if self.is_unique(cur, prev):
                    prev_unique.next = cur
                    prev_unique = cur
                    cur = cur.next
                else:
                    prev = cur
                    cur = cur.next

        prev_unique.next = None
        return dummy_head.next


s = Solution()
result = s.deleteDuplicates(head)

print(make_array(result))