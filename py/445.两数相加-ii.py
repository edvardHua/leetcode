#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1l, l2l = [], []
        while l1:
            l1l.append(l1)
            l1 = l1.next

        while l2:
            l2l.append(l2)
            l2 = l2.next
        
        inc = 0
        ans = None
        while l1l or l2l:
            l1_val = l1l.pop().val if l1l else 0
            l2_val = l2l.pop().val if l2l else 0
            s = l1_val + l2_val + inc
            inc = s // 10
            cur = ListNode(s % 10)
            cur.next = ans
            ans = cur
        
        if inc:
            cur = ListNode(1)
            cur.next = ans
            ans = cur
        
        return ans

        
# @lc code=end

