"""
Implement pow(x, n), which calculates x raised to the power n (xn).
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == -1:
            return 1 / x
        return self.myPow(x * x, n / 2) * (1 if n % 2 == 0 else x )