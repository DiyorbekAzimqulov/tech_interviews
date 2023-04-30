from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    """
    https://jamboard.google.com/d/11XPaZMu7RVaRrXNlKLKLsZA6A7EwDzCJeB5drzPO2nY/edit?usp=sharing
    """

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head and head.next is None:
            return head
        prev = head
        cur = head.next
        while cur is not None:
            if cur.val == prev.val:
                cur = cur.next
            else:
                prev.next = cur
                prev = cur
                cur = cur.next
        prev.next = None
        return head
