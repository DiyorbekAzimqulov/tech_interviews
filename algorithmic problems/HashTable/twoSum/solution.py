class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1115/
        so we iterate numbers 
        for each number
            target - num this value needs to be in the nums. if so then we need to return the index of 
            two numbers
            
        """
        seen = {}
        for idx, num in enumerate(nums):
            if (target - num) in seen:
                return [idx, seen[target-num]]
            else:
                seen[num] = idx
        