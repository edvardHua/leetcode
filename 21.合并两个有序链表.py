#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 1. 与合并排序一样，将两个链表合并
    # 2. 像连线一样连接起来
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        dummy = head
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
            elif l2.val < l1.val:
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next
        
        if l1: dummy.next = l1
        if l2: dummy.next = l2

        return head.next
        
# @lc code=end

