class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1112/
        """
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False