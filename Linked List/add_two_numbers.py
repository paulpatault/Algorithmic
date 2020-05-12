"""
You are given two linked-lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        node = self
        output = ""
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        return output


class Solution:
    def addTwoNumbers(self, l1, l2):
        l3 = dummy = ListNode(-1)
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            value = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            l3.next = ListNode(value)
            l3 = l3.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            l3.next = ListNode(1)
        return dummy.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
print(result)
# 7 0 8

