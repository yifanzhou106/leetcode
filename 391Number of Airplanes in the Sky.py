"""
391. Number of Airplanes in the Sky
中文English
Given an list interval, which are taking off and landing time of the flight. How many airplanes are there at most at the same time in the sky?

Example
Example 1:

Input: [(1, 10), (2, 3), (5, 8), (4, 7)]
Output: 3
Explanation:
The first airplane takes off at 1 and lands at 10.
The second ariplane takes off at 2 and lands at 3.
The third ariplane takes off at 5 and lands at 8.
The forth ariplane takes off at 4 and lands at 7.
During 5 to 6, there are three airplanes in the sky.
Example 2:

Input: [(1, 2), (2, 3), (3, 4)]
Output: 1
Explanation: Landing happen before taking off.

Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    def countOfAirplanes(self, airplanes):
        # write your code here
        sortedList = []
        for item in airplanes:
            sortedList.append((item.start, 1))
            sortedList.append((item.end, -1))
        sortedList.sort()
        max = 0
        sum = 0
        for item in sortedList:
            key, value = item
            sum = sum + value
            if sum > max:
                max = sum

        return max