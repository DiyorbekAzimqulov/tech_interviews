class Solution(object):
    def checkIfExist(self, arr):
        """
        https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
        :type arr: List[int]
        :rtype: bool
        [7, 14]
        0 in {0, 1, 2, 0, 4, 8, 0}
        """

        nums = set(arr)

        for num in arr:

            if num == 0:
                if arr.count(0) > 1:
                    return True

            elif num * 2 in nums:
                return True

        return False
