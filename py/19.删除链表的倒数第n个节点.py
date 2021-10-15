#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return head

        dummy = ListNode(0)
        dummy.next = head

        slow, fast = dummy, dummy
        for _ in range(0, n):
            if fast.next:
                fast = fast.next
            else:
                return head
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        if not slow.next:
            return None

        slow.next = slow.next.next
        
        return dummy.next


# @lc code=end

