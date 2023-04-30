from typing import List
"""
https://leetcode.com/problems/find-the-duplicate-number/
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        """
        there are many ways to solve this question, some of them do not meet the
        constraints but approaches presented here may help to solve similar questions
        like this.
        
        #1 approach - Sorting the input array
        #2 apporach - using hashset for keeping track of seen values.
        """
        # nums.sort()
        # if len(nums) < 2:
        #     return None
        # prev = nums[0]
        # for num in nums[1:]:
        #     print(prev, num)
        #     if prev == num:
        #         return prev
        #     else:
        #         prev = num
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        
        