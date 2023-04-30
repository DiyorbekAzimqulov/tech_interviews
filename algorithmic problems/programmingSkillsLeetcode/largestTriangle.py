from typing import List


class Solution:

    @classmethod
    def is_valid_triangle(cls, a: int, b: int, c: int):
        return a + b > c and b + c > a and a + c > b

    def largestPerimeter(self, nums: List[int]) -> int:
        """
        to form a triangle there is a rule to be satisfied
        sum of 2 sides always must be greater than the third side
        """
        nums.sort()
        maxPer = 0
        i = 0
        j = 1
        k = 2
        while k < len(nums):
            a, b, c = nums[i], nums[j], nums[k]
            if Solution.is_valid_triangle(a, b, c):
                print(a, b, c)
                maxPer = max(maxPer, sum((a, b, c)))
            i, j, k = i + 1, j + 1, k + 1
        return maxPer
