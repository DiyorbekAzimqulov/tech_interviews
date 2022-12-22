"""
https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/
"""
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        """
        1. find the maxiumum number in the list, also its index, and store them in a variable
        2. iterate over numbers and compare so that do all numbers are less than twice of the maximum
        number, if we encounter a number is not twice less than the maximum then we return -1
        otherwise we return the maximum number's index
        
        O(n) - time, O(1) - space
        """
        max_num = float("-inf")
        max_index = None
        for idx, num in enumerate(nums):
            if num > max_num:
                max_num = num
                max_index = idx
        for num in nums:
            if num != max_num and num * 2 > max_num:
                return -1
        return max_index
