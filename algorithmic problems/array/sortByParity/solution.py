from typing import List

"""
https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/
"""
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        so we need to move even integer numbers to the beginning of the array and move keep odd integer numbers to the end of the array
               |
        [2,4,3,1]
           ^
        
        """
        odd_number = 0
        cur = 0
        while cur < len(nums):
            if nums[cur] % 2 != 0:
                # current number is odd integer
                cur += 1
            else:
                # current number is even integer, 
                temp = nums[odd_number] # 2
                nums[odd_number] = nums[cur] # 2
                nums[cur] = temp # 2
                odd_number += 1
                cur += 1
        return nums