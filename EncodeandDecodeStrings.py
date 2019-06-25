
"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode
"""


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    """
    word -> :;
    :    -> ::
    """

    def encode(self, strs):
        # write your code here
        encodes = []
        for str1 in strs:
            if str1 == ':':
                encodes.append('::')
            else:
                encodes.append(str1)
            encodes.append(':;')
        return "".join(encodes)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here
        strs = []
        decode = []
        i = 0
        while i < len(str) - 1:
            if str[i] == ':':
                if str[i + 1] == ':':
                    strs.append(str[i])
                    i += 2
                elif str[i + 1] == ';':
                    strs.append("".join(decode))
                    decode = []
                    i += 2
            else:
                decode.append(str[i])
                i += 1

        return strs



