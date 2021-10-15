#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node_list = []
        dummy = head
        while dummy:
            node_list.append(dummy)
            dummy = dummy.next
        

        l, r = 0, len(node_list) - 1
        while r >= l:
            if l == r:
                # odd case
                node_list[l].next = None
            else:
                # even case
                if r == l+1:
                    node_list[r].next = None
                else:
                    node_list[l].next = node_list[r]
                    node_list[r].next = node_list[l+1]
            l += 1
            r -= 1

# @lc code=end

