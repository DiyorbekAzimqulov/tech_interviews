"""
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    def binary_to_decimal(self, binary): 
        """
        1000
        0 * 2 ^ 0 + 0 * ^ 1 + 0 * 2 ^ 2 + 1 * 2 ^ 3
        1 0 1
        """
        result = 0
        two_power = 0
        while binary:
            last = binary % 10  # 1
            result += last * (2 ** two_power)
            binary = binary // 10
            two_power += 1
        return result
            
    
    def getDecimalValue(self, head: ListNode) -> int:
        """
        1 0 1
        """
        binary = 0
        cur = head
        while cur:
            binary = binary * 10
            binary += cur.val
            cur = cur.next
        print(binary)
        return self.binary_to_decimal(binary)