class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/single-number/solutions/1771771/think-it-through-time-o-n-space-o-1-python-explained/
        """
        hash_table = {}
        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
                continue
            hash_table[num] = 1
        for k, v in hash_table.items():
            if v == 1:
                return k