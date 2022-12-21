class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        create leftSum array where we store elements sum left to the current element
        create rightSum array where we store elements sum right to the current element
        https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/
        
        """
        leftSum = [None for num in nums]
        i = 0
        curSum = 0
        while i < len(nums):
            leftSum[i] = curSum
            curSum += nums[i]
            i += 1
        rightSum = [None for num in nums]
        i = len(nums) - 1
        curSum = 0
        while i >= 0:
            rightSum[i] = curSum
            curSum += nums[i]
            i -= 1
        
        i = 0
        while i < len(nums):
            if rightSum[i] == leftSum[i]:
                return i
            i += 1
        return -1
