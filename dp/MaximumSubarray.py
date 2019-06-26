"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -2 ** 32
        presum = nums[0]

        for i in range(1, len(nums)):
            presum = max(nums[i], presum + nums[i])
            res = max(res, presum)
        res = max(res, nums[0])
        return res