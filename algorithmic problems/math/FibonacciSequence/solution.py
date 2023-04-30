"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

https://leetcode.com/problems/fibonacci-number/
"""
class Solution:
    def fib(self, n: int) -> int:
        """
        first fib is 0
        second fib is 1
        third fib is first + second 
        
        we are going to use recursion to find the fibonacci sequence
        base case:
        if fib(0) return 0
        if fib(1) return 1
        
        """
        
        if n == 0: return 0
        if n == 1: return 1
        return self.fib(n-1) + self.fib(n - 2)
    