class Solution:
    
    def number_digit_square(self, n: int) -> int:
        s = 0
        while n != 0:
            digit = n % 10
            s += digit ** 2
            n //= 10
        return s
    
    def isHappy(self, n: int) -> bool:
        """
        https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1131/
        there are two cases might happen
        1. we eventually get to 1
        2. we cycle over numbers we already seen
        if we cycle then we return false
        """
        seen = set()
        while True:
            n = self.number_digit_square(n)
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
