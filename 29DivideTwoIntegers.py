"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Input: dividend = 10, divisor = 3
Output: 3

"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend >= 0 and divisor >= 0) or (dividend <= 0 and divisor <= 0):
            isPos = True
        else:
            isPos = False

        if divisor == -1 and dividend == -2 ** 31:
            return 2 ** 31 - 1

        elif divisor == 1:
            return abs(dividend) if isPos  else -abs(dividend)

        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        if abs_dividend < abs_divisor:
            return 0

        q = 1
        rq = 0
        d = abs_divisor
        while True:
            t = abs_divisor << 1
            if t < abs_dividend:
                abs_divisor = t
                q += q
            else:
                rq += q
                q = 1
                abs_dividend -= abs_divisor

                abs_divisor = d
                if abs_dividend < (abs_divisor << 1):
                    if abs_dividend >= abs_divisor:
                        rq += 1
                    break

        return rq if isPos else -rq
