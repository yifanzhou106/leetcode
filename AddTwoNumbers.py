"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(-1)
        head = res
        carry = 0
        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + carry
            carry = sum / 10
            sum %= 10
            cur = ListNode(sum)
            res.next = cur
            res = cur
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            sum = l1.val + carry
            carry = sum / 10
            sum %= 10
            cur = ListNode(sum)
            res.next = cur
            res = cur
            l1 = l1.next

        while l2 is not None:
            sum = l2.val + carry
            carry = sum / 10
            sum %= 10
            cur = ListNode(sum)
            res.next = cur
            res = cur
            l2 = l2.next
        if carry != 0:
            cur = ListNode(1)
            res.next = cur
        return head.next