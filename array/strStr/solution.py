class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1161/
        we use two pointer technique here. 
        one pointer for haystack 
        another pointer needle
        
        we iterate until pointer to haystack or needle exceeds
        if haystack exceeds then we return -1
        otherwise we return the index where needle starts
        
        while iterating we also store starting position of needle
        
        
        sadbutsad
        |  ^
        sad
           ^
        
        """
        i = 0
        j = 0
        idx = None
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                if idx is None:
                    idx = i
                i += 1
                j += 1
            else:
                if idx is None:
                    i += 1
                j = 0
                if idx is not None:
                    i = idx + 1
                idx = None
        if i == len(haystack) and j < len(needle):
            return -1
        return idx if idx is not None else -1

b = "mississippi"
a = "issip"

sol = Solution()
print(sol.strStr(a, b))