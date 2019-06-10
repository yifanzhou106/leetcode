"""
Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s = sorted(nums)
        result = 0
        minDiff = float("inf")
        minNums = list()

        for k in range (len(s)):
            i = k + 1
            j = len(s) - 1
            while i < j:

                sum = s[k] + s[i] + s[j]
                diff = abs(target - sum)
                if minDiff > diff:
                    minDiff = diff
                    minNums.clear()
                    minNums.append(s[k])
                    minNums.append(s[i])
                    minNums.append(s[j])
                    result = sum
                if sum < target:
                    i += 1
                elif sum > target:
                    j -= 1
                else:
                    break


        print(minNums)
        return result

nums = [1,1,-1,-1,3]
print(Solution().threeSumClosest(nums,1))

nums2 = [-1,2,1,-4]
print(Solution().threeSumClosest(nums2,1))