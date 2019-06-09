"""
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution(object):
    numdict ={
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }

    """
    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.
    499 = CDXCIX
    399 = CCCXCIX
    799 = 700 + 90 + 9 = DCC + XC + IX = DCCXCIX
    """
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romanNum = ''
        reminder, romanNum = self.greaterThanM(num,romanNum)

        reminder, romanNum = self.CToM(reminder,romanNum)

        reminder, romanNum = self.XToC(reminder,romanNum)

        romanNum = self.IToX(reminder, romanNum)
        return romanNum

    def greaterThanM(self,num,str):
        reminder = num % 1000
        num = int(num / 1000)
        if num > 0:
            for i in range(num):
                str += self.numdict.get(1000)
        return reminder,str

    def CToM(self,num,str):
        reminder = num % 100
        num = int(num / 100)

        if num < 4:
            for i in range(num):
                str += self.numdict.get(100)
        elif num is 4:
            str += self.numdict.get(100)
            str += self.numdict.get(500)
        elif num >4 and num < 9:
            str += self.numdict.get(500)
            for i in range(num - 5):
                str += self.numdict.get(100)
        elif num is 9:
            str += self.numdict.get(100)
            str += self.numdict.get(1000)
        return reminder,str

    def XToC(self,num,str):
        reminder = num % 10
        num = int(num / 10)

        if num < 4:
            for i in range(num):
                str += self.numdict.get(10)
        elif num is 4:
            str += self.numdict.get(10)
            str += self.numdict.get(50)
        elif num >4 and num < 9:
            str += self.numdict.get(50)
            for i in range(num - 5):
                str += self.numdict.get(10)
        elif num is 9:
            str += self.numdict.get(10)
            str += self.numdict.get(100)
        return reminder,str

    def IToX(self,num,str):
        if num < 4:
            for i in range(num):
                str += self.numdict.get(1)
        elif num is 4:
            str += self.numdict.get(1)
            str += self.numdict.get(5)
        elif num >4 and num < 9:
            str += self.numdict.get(5)
            for i in range(num - 5):
                str += self.numdict.get(1)
        elif num is 9:
            str += self.numdict.get(1)
            str += self.numdict.get(10)
        return str


num = 799
str = Solution().intToRoman(num)
print(str)