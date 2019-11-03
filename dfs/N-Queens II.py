class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = 0
        self.colValid = []
        self.crossValid = []
        self.cross2Valid = []
        self.dfs(0, n)
        return self.result

    def dfs(self, row, n):
        if row == n:
            self.result += 1
            return

        for i in range(n):
            if not self.isValid(row, i):
                continue

            self.colValid.append(i)
            self.crossValid.append(row - i)
            self.cross2Valid.append(row + i)
            self.dfs(row + 1, n)

            self.colValid.pop()
            self.crossValid.pop()
            self.cross2Valid.pop()

    def isValid(self, row, i):
        return (i not in self.colValid) and (row - i not in self.crossValid) and (row + i not in self.cross2Valid)
