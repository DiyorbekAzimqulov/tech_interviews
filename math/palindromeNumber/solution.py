class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        121 -> 121
        result = 0
        digit = 1
        result += digit
        result = 1
        result *= 10
        result = 10
        digit = 2
        result += digit
        result = 12
        
        """
        n = x
        result = 0
        while x > 0:
            digit = x % 10
            result += digit
            result *= 10
            x //= 10
        result //= 10

        return result == n

s = Solution()
print(s.isPalindrome(-121))