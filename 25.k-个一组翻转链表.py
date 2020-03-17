#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def _is_possible(self, node, k):
        for _ in range(k):
            node = node.next
            if node is None:
                return False
        return node

    def _do_reverse(self, node):
        prev, cur = None, node
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev, node

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        prev, prev.next = self, head

        while True:
            end = self._is_possible(prev, k)
            if not end:
                break
            
            group_next = end.next
            end.next = None
            start, end  = self._do_reverse(prev.next)

            prev.next = start
            end.next = group_next

            prev = end

        return self.next

# @lc code=end

