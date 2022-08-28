from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        we need at least 3 search place
        """
        if len(nums) < 1:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        # keep search space at least 3
        start = -1
        # find starting position
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                # check starting position is on the right or left
                if nums[mid-1] == target: # 3 search place
                    # start is on the left
                    right = mid
                else:
                    start = mid
                    break
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        # need to make preprocess
        if start == -1:
            if nums[left] == target:
                start = left
            elif nums[right] == target:
                start = right


        left, right = 0, len(nums) - 1
        end = -1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                # check starting position is on the right or left
                if nums[mid+1] == target: # 3 search place
                    # start is on the left
                    left = mid
                else:
                    end = mid
                    break
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        # need to make preprocess
        if end == -1:
            if nums[right] == target:
                end = right
            elif nums[left] == target:
                end = left
        return [start, end]