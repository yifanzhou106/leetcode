class Solution:
    def subarraySum(self, nums):
        map, prefix_sum = {0: 0}, 0
        for i, n in enumerate(nums):
            prefix_sum += n
            if prefix_sum in map:
                return map[prefix_sum], i
            map[prefix_sum] = i + 1
        print(map)


list1 = [-3, 1, 2, -3, 4]
print(Solution().subarraySum(list1))