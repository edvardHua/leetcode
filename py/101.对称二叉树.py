#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def is_mirror(self, left, right):
        if not left and not right: return True
        if not left or not right: return False

        return left.val == right.val and \
            self.is_mirror(left.left, right.right) and \
                self.is_mirror(left.right, right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        # 递归和非递归都可以解决
        # 非递归会麻烦点
        return self.is_mirror(root, root)

# @lc code=end

