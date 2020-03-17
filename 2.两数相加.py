#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        cur = dummy
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            s = x + y
            carry = s // 10

            cur.next = ListNode(s % 10)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
            
        if carry: cur.next = ListNode(1)
        return dummy.next

# @lc code=end

