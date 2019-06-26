"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""



class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 0:
            return

        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = i + (j - i) / 2
            # print i, j,mid

            if len(nums) < 0:
                return

            i = 0
            j = len(nums) - 1

            while i <= j:
                mid = i + (j - i) / 2
                # print i, j,mid

                if nums[mid] == target:
                    return mid
                elif nums[mid] <= nums[j]:
                    if nums[mid] < target <= nums[j]:
                        i = mid + 1
                    else:
                        j = mid - 1

                elif nums[mid] >= nums[i]:
                    if nums[i] <= target < nums[mid]:
                        j = mid - 1
                    else:
                        i = mid + 1

            return -1

