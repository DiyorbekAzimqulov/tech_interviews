from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """
        https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
        [1, 2, 3, 4, 5, 3, 1, 0]
                              
        [1, 2, 3, 5, 6, 3, 4]
                        |  |
                        [1, 2, 1]
                        [2, 0, 2]   
                            |  |
        """
        if len(arr) < 3:
            return False
        
        # find peak 
        i = 0
        while i < len(arr) - 1 and arr[i] < arr[i+1]:
            i += 1
        
        # check if peak is first or last element
        if i == 0 or i == len(arr) - 1:
            return False
        
        # we found peak i = peak
        while i < len(arr) - 1 and arr[i] > arr[i+1]:
            i += 1
        return i == len(arr) - 1