"""
https://leetcode.com/problems/day-of-the-year/
"""

class Solution:
    
    def isLeapYear(self, year: int) -> bool:
        """
        returns whether given year is a leap year or not
        what is leap year
        
        - given year is divided into 400
        - given year divided into 4 but not 100
        
        since we have range between 1900 to 2019 we do not need to divide year by 400
        """
        if year % 400 == 0:
            return True
        return year % 100 != 0 and year % 4 == 0
    
    
    def dayOfYear(self, date: str) -> int:
        """
        need to identify how many days passed since beginning of the year.
        in leap year february gets added 1 day additional
        
        we need to have
        1. function which returns given year is a leap year or not
        2. hash map which maps month number to number of days
        """
        mapping = {
            1: 31,
            2: 28,  # considering it is not a leap year
            3: 31,
            4: 30,
            5: 31, 
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        year = date[:4]
        month = date[5:7]
        day = date[8:10]
        print(year, month, day)
        if self.isLeapYear(int(year)):
            mapping[2] = 29
        
        days = 0
        for m in range(1, int(month)):
            days += mapping[m]
        days += int(day)
        return days

date_ = "2003-03-01"
solution = Solution()
print(solution.dayOfYear(date_))