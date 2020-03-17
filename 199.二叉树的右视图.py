#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []

        ans = []
        q = [root]
        # BFS, get latest elem val in each layer
        while q:
            ql = len(q)
            for _ in range(ql):
                elem = q.pop(0)
                if elem.left: q.append(elem.left)
                if elem.right: q.append(elem.right)
            ans.append(elem.val)
        return ans

# @lc code=end

