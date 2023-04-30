"""
https://leetcode.com/problems/counting-bits/
"""
from typing import List
class Solution:
    
    def numberOfOne(self, n):
        res = 0
        while n:
            res += n % 2
            n //= 2
        return res
    
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            result.append(self.numberOfOne(i))
        return result