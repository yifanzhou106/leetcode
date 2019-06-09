"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        count = 0
        numbers = list()
        result = 0
        possitive = True
        isSquence = True
        isSignUsed = False

        for c in str:
            if ord(c) is 32 and count == 0:
                continue
            elif ord(c) is 43 and count == 0:
                possitive = True
                isSignUsed = True
                count = count + 1
            elif ord(c) is 45 and count == 0:
                possitive = False
                isSignUsed = True
                count = count + 1
            elif (ord(c) >= 48 and ord(c) <= 57) and isSquence == True:
                count = count + 1
                numbers.append(ord(c) - 48)
            elif (count is not 0) and (ord(c) < 48 or ord(c) > 57):
                isSquence = False
                break
            elif count is 0:
                break

        if count is not 0:
            if isSignUsed == True:
                count = count - 1
            result = self.buildNumber(numbers, count, possitive)

        return result

    def buildNumber(self, numbers, count, possitive):
        result = 0
        for num in numbers:
            result += num * 10 ** (count - 1)
            count -= 1
        if result >= 2 ** 31:
            if possitive is False:
                result = 2 ** 31
            else:
                result = 2 ** 31 - 1
        if possitive is False:
            result = -result

        return result

