"""
https://leetcode.com/problems/intersection-of-two-arrays/
"""

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        find intersection of two array.
so what intersection of two array mean?
elements in array1 are also present in array2
we gather common elements to a new array and return it.
if we use 2 nested loop, and compare elements from first array to the second array and store values to a new array we can have solution
time O(n^2)
space O(n)

if we convert two arrays to sets which gives **in/contains** operations in O(1) time. we are going to have solution which its time and space complexity as follows:
time -> O(n + m) where **n** is the lenght of the first array and **m** is the length of the second array.
space -> O(1)
        """
        # very naive approach: brute-force
        # result = set()
        # for num1 in nums1:
        #     for num2 in nums2:
        #         if num1 == num2:
        #             result.add(num1)
        #             break
        # return list(result)
        
        # using set theory
        nums1 = set(nums1)
        nums2 = set(nums2)
        # to save some time complexity we iterate array which has smaller length
        if len(nums1) < len(nums2):
            return [num for num in nums1 if num in nums2]
        return [num for num in nums2 if num in nums1]
