class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        1. pointer to last element
        2. add one to last element
        3. store this value mod 10 to its position
        if we have parity
            decrement pointer
            step 2
        if at the end we also have parity we insert 1 to 0th index
        
        [9, 9, 9]
         ^
        https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/
        """
        current = len(digits) - 1
        num = 1
        while current >= 0:
            new_digit = (digits[current] + num) # 9 + 1 == 10
            if new_digit // 10 >= 1: # yes
                # digit is greater than 9
                digits[current] = new_digit % 10 # [1, 0, 0, 0]
                current -= 1
            else:
                digits[current] = new_digit # [1,2,4]
                break
        if current < 0: # no
            digits.insert(0, 1)
        return digits
