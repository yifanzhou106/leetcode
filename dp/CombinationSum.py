"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.recFunc(candidates, target, [], candidates[0])

    def recFunc(self, can, target, path, minCan):

        res = []
        for i in range(len(can)):
            diff = target - can[i]
            if diff >= minCan:
                res += self.recFunc(can[i:], diff, path + [can[i]], can[i])
            elif diff == 0:
                res += [path + [can[i]]]
        return res


