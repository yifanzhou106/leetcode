"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.


"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        nums = [0] * (len(num1) + len(num2))
        j = len(num1) - 1
        i = len(num2) - 1
        while i >= 0:
            j = len(num1) - 1
            while j >= 0:
                n1 = ord(num1[j]) - ord('0')
                n2 = ord(num2[i]) - ord('0')
                nums[i + j + 1] += n1 * n2
                j -= 1
            i -= 1
        # 0 81 81
        i = len(nums) - 1
        carry = 0
        while i >= 0:
            sum1 = nums[i] + carry
            nums[i] = sum1 % 10
            carry = sum1 / 10
            i -= 1

        res = ''
        isFirstZero = True
        for num in nums:
            if num == 0 and isFirstZero:
                continue
            isFirstZero = False
            res = res + str(num)

        if len(res) == 0:
            return '0'
        return res

