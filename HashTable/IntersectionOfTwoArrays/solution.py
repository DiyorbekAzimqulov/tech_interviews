class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1105/
        to find the intersection of two arrays, we can see them as sets and we take the intersection of
        two sets and return the result
        """
        return list(set(nums1) & set(nums2))