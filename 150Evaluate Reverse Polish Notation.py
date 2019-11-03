"""
Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""


import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 0: return 0

        stack = []
        i = 0
        while True:
            if i == len(tokens): break
            if self.is_int(tokens[i]):
                stack.append(int(tokens[i]))
            elif tokens[i] == '+' or tokens[i] == '-' or tokens[i] == '*' or tokens[i] == '/':
                b = stack.pop()
                a = stack.pop()
                if tokens[i] == '+':
                    stack.append(a + b)
                elif tokens[i] == '-':
                    stack.append(a - b)
                elif tokens[i] == '*':
                    stack.append(a * b)
                elif tokens[i] == '/':
                    # print(a, b, math.trunc(a/float(b)))
                    stack.append(math.trunc(a / float(b)))
            i += 1
            # print stack

        return stack.pop()

    def is_int(self, str):
        try:
            int(str)
            return True
        except ValueError:
            return False
