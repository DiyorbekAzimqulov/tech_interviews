class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        """
        https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1154/
        if we sort given array and pair them from the beginning then we get our result
        """
        nums.sort()
        s = 0
        j = 1
        while j < len(nums):
            s += min(nums[j-1], nums[j])
            j += 2
        return s
