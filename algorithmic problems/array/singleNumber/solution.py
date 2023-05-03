"""
https://leetcode.com/problems/single-number/description/
"""


class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        """
        XOR order does not matter. we have duplicate values except one. if we XOR all 
        values then we are left with unique value!
        """
        result = 0
        for num in nums:
            result ^= num
        return result