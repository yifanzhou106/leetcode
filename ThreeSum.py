"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = sorted(nums)
        result = set()
        for k in range(len(s)):
            target = -s[k]
            i = k + 1
            j = len(s)-1

            while i < j:
                if (s[i]+s[j])<target:
                    i += 1
                elif (s[i]+s[j])>target:
                    j -= 1
                else:
                    result.add((s[k],s[i],s[j]))
                    i += 1
                    j -= 1

        return result

nums = [-4,-1,-1, 0, 1, 2]
print(Solution().threeSum(nums))