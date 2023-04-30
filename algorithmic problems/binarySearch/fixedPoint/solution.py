class Solution:
    def solve(self, nums):
        def helper(nums, left, right, cur_min):
            mid = (left + right) // 2
            if nums[mid] == mid:
                if cur_min > mid:
                    cur_min = mid
            if left == right:
                return
            helper(nums, left, mid, cur_min)
            helper(nums, mid, right, cur_min)
        min_ = float('+inf')
        helper(nums, 0, len(nums)-1, min_)
        if min_ == float('+inf'):
            return -1
        return min_
        
nums = [-5, -3, 0, 3, 4]
s = Solution()
print(s.solve(nums))