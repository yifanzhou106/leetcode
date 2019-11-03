"""
Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
"""

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dir = {}
        for i in words:
            if i in dir:
                dir[i] += 1
            else:
                dir[i] = 1
        heap = []
        # heapq.heapify(heap)
        for key in dir:
            heapq.heappush(heap, (-dir[key], key))
        aws = []
        for i in range(k):
            aws.append(heapq.heappop(heap)[1])
        # aws.sort()
        return aws
