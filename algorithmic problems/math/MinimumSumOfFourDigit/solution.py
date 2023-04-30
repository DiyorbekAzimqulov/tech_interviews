class Solution:
    
    def min_digit(self, num: int, last_min: float) -> int:
        """
        finds minimum digit from the number, and removes that digit from the number
        returns minimum digit
        """
        cur_min = float('inf')
        prev_min = float('inf')
        number = 0
        while num != 0:
            digit = num % 10
            if digit < cur_min:
                if cur_min != float('inf'):
                    number += cur_min
                    number *= 10
                prev_min = cur_min
                cur_min = digit
            else:
                number += digit
                number *= 10
            num //= 10
        if cur_min == last_min:
            return last_min, number // 10
        return cur_min, number // 10

    def minimumSum(self, num: int) -> int:
        """
        find two minimum digit from number, 
        set them as leading digits of new1 and new2.
        obtain last digits and add them. that will be the possible minimum sum
        """
        new1 = 0
        new2 = 0
        for i in range(4):
            cur_min, num = self.min_digit(num, float('inf'))
            if i == 0:
                new1 = cur_min
                new1 *= 10
            elif i == 1:
                new2 = cur_min
                new2 *= 10
            elif i == 2:
                new1 += cur_min
            else:
                new2 += cur_min
        return new1 + new2
num = 8100
solution = Solution()
print(solution.minimumSum(num))