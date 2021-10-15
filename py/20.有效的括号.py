#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 妈的，空字符串竟然是返回 True
        if not s:
            return True

        my_stack = []
        match_val = {")": "(", "}": "{", "]":"["}

        for c in s:
            if c in match_val and len(my_stack) > 0:
                bracket = my_stack.pop()
                if bracket != match_val[c]:
                    return False
            else:
                my_stack.append(c)

        return False if len(my_stack) != 0 else True
        
# @lc code=end
