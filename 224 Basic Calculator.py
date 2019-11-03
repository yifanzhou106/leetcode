"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, num, sign, stack = 0, 0, 1, [1]

        for i in s + '+':
            if i.isdigit():
                # print num
                num = num * 10 + int(i)
            elif i in '+-':
                res += num * sign * stack[-1]
                if i == '+':
                    sign = 1
                else:
                    sign = -1
                num = 0
            elif i == '(':
                stack.append(sign * stack[-1])
                sign = 1

            elif i == ')':
                res += num * sign * stack[-1]
                num = 0
                stack.pop()

        return res

