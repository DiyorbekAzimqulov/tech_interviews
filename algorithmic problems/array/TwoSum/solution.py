class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1153/
        since we are given sorted array, we use two pointer technique here.
        one pointer from start
        one pointer from end
        we add two pointer numbers
        if the sum is less than target
            we increment our start pointer
        if the sum is greater than target
            we decrement our end pointer
        if it is equal
            return start and end index
        this loop continues untill start and end pointer reach each other.
        O(1) space
        O(n) time
        """
        start = 0
        end = len(numbers) - 1
        while start < end:
            cur_sum = numbers[start] + numbers[end]
            if cur_sum == target:
                return [start+1, end+1]
            elif cur_sum < target:
                start += 1
            else:
                end -= 1
        