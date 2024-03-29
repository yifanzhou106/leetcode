"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.


"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map1 = {}
        map2 = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in map1:
                map1[s[i]] = i + 1
            if t[i] not in map2:
                map2[t[i]] = i + 1

            if map1[s[i]] != map2[t[i]]:
                return False

        return True