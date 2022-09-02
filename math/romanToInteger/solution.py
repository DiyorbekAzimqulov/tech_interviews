class Solution:
    def romanToInt(self, s: str) -> int:
        """
        roman numbers written from largest to smallest, it means larger values come
        first. some times it is not always the case. if we encounter smaller value             came first than larger value, it means there is subtraction happened.
        
        we iterate roman number as string from back to front, and add correspoding             value of roman character to our result variable.
        since we might have smaller value come first than larger value, we need to
        check whether we have smaller value come first.
        """
        r_i_map = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        right = len(s) - 1
        result = 0
        while right > 0:
            # check we have not smaller value
            if r_i_map[s[right-1]] < r_i_map[s[right]]:  # we encountered subtraction value
                roman_number = s[right-1] + s[right]
                int_value = r_i_map[roman_number]
                result += int_value
                right -= 2
            else:  # normal value
                roman_number = s[right]
                int_value = r_i_map[roman_number]
                result += int_value
                right -= 1
        if right == 0:
            result += r_i_map[s[right]]
        return result


string = "CM"
s = Solution()
print(s.romanToInt(string))