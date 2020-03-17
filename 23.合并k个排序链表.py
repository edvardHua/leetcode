#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from queue import PriorityQueue

class Solution:
    # 1. 暴力法，把全部元素放到数组里，然后排序，最后再转成链表
    # 把元素放进数组，复杂度 N，稳定排序算法，复杂度 NlogN，最后转成链表，复杂度 N
    # 2. 采用合并排序，每次合并时间复杂度为 N，总共需要合并 logk，k 为链表个数，总的时间复杂度
    # 为 Nlogk
    def mergeKLists(self, lists):
            """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next


# @lc code=end

