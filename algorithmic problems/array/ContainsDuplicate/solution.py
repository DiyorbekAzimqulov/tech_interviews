from typing import List
"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

https://leetcode.com/problems/contains-duplicate-ii/
"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        nums = [1,2,3,1], k = 3
        use hash table to store unique numbers as number, index
        if iteration number is in the hash table then we check their absolute 
        difference of indecies values, if value exceeds limit we update value with greater.
        """
        
        table = {}
        for idx, num in enumerate(nums):
            if num not in table:
                table[num] = idx
            else:
                first_idx = table[num]
                if abs(first_idx - idx) <= k:
                    return True
                else:
                    table[num] = idx
        return False
