"""
https://leetcode.com/problems/add-strings/
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        456 + 77
        ^    ^
        533 :1
        """
        r1 = len(num1) - 1
        r2 = len(num2) - 1
        result = ""
        carry = 0
        while r1 >= 0 and r2 >= 0:
            num = int(num1[r1]) + int(num2[r2]) + carry
            carry = 0
            if num > 9:
                carry = num // 10
                result = str(num % 10) + result
            else:
                num += carry
                if num > 9:
                    carry = num // 10
                    result = str(num % 10) + result
                else:
                    result = str(num) + result
                    carry = 0
            r1 -= 1
            r2 -= 1
        
        while r1 >= 0:
            num = int(num1[r1]) + carry
            carry = 0
            if num > 9:
                carry = num // 10
                result = str(num % 10) + result
            else:
                result = str(num) + result
                carry = 0
            r1 -= 1
        while r2 >= 0:
            num = int(num2[r2]) + carry
            carry = 0
            if num > 9:
                carry = num // 10
                result = str(num % 10) + result
            else:
                result = str(num) + result
                carry = 0
            r2 -= 1
        if carry != 0:
            result = str(carry) + result
        return result


num1 = "237"
num2 = "284"
solution = Solution()
print(solution.addStrings(num1, num2))
