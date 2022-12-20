"""
https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/discuss/344583/Python:-O(1)-space-solution
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counter = {n:0 for n in range(1, len(nums)+1)}
        
        for num in nums:
            counter[num] += 1
        result = []
        for k, v in counter.items():
            if v == 0:
                result.append(k)
        return result
