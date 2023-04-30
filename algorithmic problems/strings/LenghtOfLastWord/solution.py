"""
https://leetcode.com/problems/length-of-last-word/
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        we have been given string s and we have to find the lenght of the last word
        
        word -> non-space character.
        if we loop this string in reverse order from encountering character untill
        encountering whitespace, so that will be the length of the last word
        """
        length = 0
        right = len(s) - 1
        while right >= 0:
            if not s[right].isalpha() and length == 0:
                right -= 1
                continue
            elif s[right].isalpha():
                right -= 1
                length += 1
            else:
                break
        return length
