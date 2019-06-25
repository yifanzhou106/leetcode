"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        head = 0
        tail = len(nums) - 1
        res = (head + tail) / 2
        if nums[-1] < target:
            return len(nums)
        if nums[0] > target:
            return 0
        while head <= tail:
            res = index = (head + tail) / 2
            if nums[index] == target:
                return index
            if nums[index] > target:
                tail = index - 1
            if nums[index] < target:
                head = index + 1
        if nums[res] < target:
            return res + 1

        return res
