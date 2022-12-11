class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/
           |
        [0,1,2,3,4,2,2,3,3,4]
                 ^         ^       
        """
        cur = 1
        unique = 0
        while cur < len(nums):
            if nums[unique] == nums[cur]:
                cur += 1
            else:
                unique += 1
                nums[unique] = nums[cur]
                cur += 1
        return unique + 1
