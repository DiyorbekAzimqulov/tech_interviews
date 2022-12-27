class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1162/
        work on two strings at a time 
        in each iteration, we have two pointers for each of the string
        if chars are equal then we add it to cur_long_pref variable
        
        """
        pref = strs[0]
        i = 1
        while i < len(strs):
            word = strs[i]
            p = 0
            cur_pref = ''
            while p < len(pref) and p < len(word):
                if pref[p] == word[p]:
                    cur_pref += pref[p]
                    p += 1
                else:
                    break
            pref = cur_pref
            i += 1
        return pref