class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        swap,unswap = [0] * len(A), [0] * len(A)
        swap[-1] = 1
        i = len(A) - 2
        while i >= 0:
            if A[i] < A[i+1] and A[i] < B[i+1] and B[i] < A[i+1] and B[i] < B[i+1]:
                swap[i] = 1 + min(swap[i+1],unswap[i+1])
                unswap[i] = 0 + min(swap[i+1],unswap[i+1])
            elif A[i] >= A[i+1] or B[i] >= B[i+1]:
                swap[i] = 1 + unswap[i+1]
                unswap[i] = 0 + swap[i+1]
            elif A[i] >= B[i+1] or B[i] >= A[i+1]:
                swap[i] = 1 + swap[i+1]
                unswap[i] = 0 + unswap[i+1]
            i -= 1
        return min(swap[0],unswap[0])