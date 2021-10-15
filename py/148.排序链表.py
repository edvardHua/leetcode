#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 1. 合并排序，递归和非递归的方法
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        slow, fast = head, head.next
        # 只需要判断 fast 就行了
        while slow and fast.next:
            slow, fast = slow.next, fast.next.next
        
        mid, slow.next = slow.next, None

        left, right = self.sortList(head), self.sortList(mid)

        h = dummy = ListNode(0)
        while left and right:
            if left.val < right.val: dummy.next, left = left, left.next
            else: dummy.next, right = right, right.next

            dummy = dummy.next
        
        dummy.next = left if left else right
        return h.next

# @lc code=end

