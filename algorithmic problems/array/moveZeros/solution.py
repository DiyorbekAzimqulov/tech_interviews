from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/
        Do not return anything, modify nums in-place instead.
        Given an integer array nums, move all 0's to the end of it while maintaining the relative order 
        of the non-zero elements.
        
        1. place non-zero elements at the beginning of array
        we iterate over the array
        if current element is zero then we find non-zero element to its right and swap them
        this algorithm is O(n) - time and O(1) - space
        """
        
        cur = 0
        non_zero = 0
        while cur < len(nums):
            if nums[cur] == 0:
                cur += 1
            else:
                temp = nums[non_zero]
                nums[non_zero] = nums[cur]
                nums[cur] = temp
                non_zero += 1
                cur += 1
        return nums
                
nums = [0,1,0,3,12]
solution = Solution()
print(solution.moveZeroes(nums))