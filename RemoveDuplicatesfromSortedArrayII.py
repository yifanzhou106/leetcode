"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        if not len(nums):
            return 0
        prenum = nums[0]
        index = 0
        while nums[index] is not None:
            num = nums[index]
            if num != prenum:
                prenum = num
                count = 0
            if count < 2:
                count = count + 1
                index += 1
            else:
                del nums[index]
            if index > len(nums) - 1:
                break

        return len(nums)
