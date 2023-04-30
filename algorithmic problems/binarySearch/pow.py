class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(base, power):
            if base == 0:
                return 0
            if power == 0:
                return 1
            if power == 1:
                return base
            result = helper(base, power // 2)
            result = result * result
            return base * result if power % 2 else result
        result = helper(x, abs(n))
        return result if n >= 0 else 1 / result

power = 10000
base = 10
s = Solution()
print(s.myPow(base, power))