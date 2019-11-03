"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left = 0
        right = 0
        res = []

        for c in s:
            if left == 0:
                if c == ')':
                    right += 1
                elif c == '(':
                    left += 1
            else:
                if c == ')':
                    left -= 1
                elif c == '(':
                    left += 1
        self.dfs(left, right, s, 0, res)
        return res

    def isValid(self, s):
        left = 0
        right = 0
        for c in s:
            if left == 0:
                if c == ')':
                    right += 1
                elif c == '(':
                    left += 1
            else:
                if c == ')':
                    left -= 1
                elif c == '(':
                    left += 1
        return True if left + right == 0 else False

    def dfs(self, l, r, s, index, res):
        if (l == 0 and r == 0):
            if self.isValid(s) and s not in res:
                res.append(s)
            return
        for i in range(index, len(s)):
            if i > 0 and s[i] == s[i - 1]:
                continue
            if l > 0 and s[i] == '(':
                self.dfs(l - 1, r, s[:i] + s[i + 1:], i, res)
            elif r > 0 and s[i] == ')':
                self.dfs(l, r - 1, s[:i] + s[i + 1:], i, res)

