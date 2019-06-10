"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = list()
        str = [""] * 2 * n
        self.rec(results,str,0,n,0,0)
        return results

    def rec(self,results, str, pos, n, open, close):
        if close is n:
            str1 = ''.join(str)
            results.append(str1)
            return
        else:
            if open > close:
                str[pos] = ")"
                self.rec(results, str, pos + 1, n, open, close + 1)
            if open < n:
                str[pos] = "("
                self.rec(results, str, pos + 1, n, open + 1, close)

n=3
print(Solution().generateParenthesis(n))