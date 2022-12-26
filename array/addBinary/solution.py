class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1160/
        1 solution
        convert binary to decimal for both string
        add them
        convert this result to binary
        return it as string.
        2 solution
        using two pointers which pointing to the last element of each string, 
        we can add together them. string concatenation happends.
        """
        result = []
        i = len(a) - 1
        j = len(b) - 1
        parity = 0
        while i >= 0 and j >= 0:
            num = int(a[i]) + int(b[j]) + parity
            if num != 0 and num % 2 == 0:
                parity = 1
                result.insert(0, '0')
            elif num == 0:
                parity = 0
                result.insert(0, '0')
            elif num == 1:
                parity = 0
                result.insert(0, '1')
            else:
                parity = 1
                result.insert(0, '1')
            

            i -= 1
            j -= 1
        
        while i >= 0:
            num = int(a[i]) + parity
            if num != 0 and num % 2 == 0:
                parity = 1
                result.insert(0, '0')
            elif num == 0:
                parity = 0
                result.insert(0, '0')
            elif num == 1:
                parity = 0
                result.insert(0, '1')
            else:
                parity = 1
                result.insert(0, '1')
            i -= 1
        while j >= 0:
            num = int(b[j]) + parity
            if num != 0 and num % 2 == 0:
                parity = 1
                result.insert(0, '0')
            elif num == 0:
                parity = 0
                result.insert(0, '0')
            elif num == 1:
                parity = 0
                result.insert(0, '1')
            else:
                parity = 1
                result.insert(0, '1')
            j -= 1
        if parity != 0:
            result.insert(0, '1')
        return "".join(result)



b = '1111'
a = '1111'
sol = Solution()
print(sol.addBinary(a, b))