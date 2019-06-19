"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        cache = {}
        return self.recMovement(m, n, cache)

    def recMovement(self, m, n, cache):
        if (m, n) in cache:
            return cache[(m, n)]

        if m == 1 or n == 1:
            return 1

        cache[(m, n)] = self.recMovement(m - 1, n, cache) + self.recMovement(m, n - 1, cache)

        return cache[(m, n)]


print(Solution().uniquePaths(100,100))