#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # 两种办法，第一种是暴力法
        # 第二种方法和暴力一样，但是添加了记忆
        l, r = [], []
        hl = len(height)
        for i in range(0, hl):
            if i == 0: 
                l.append(0)
                continue
            l.append(max(height[0:i]))
        
        for i in range(0, hl):
            if i == hl - 1:
                r.append(0)
                continue
            r.append(max(height[i+1:]))

        s = 0
        for i, h in enumerate(height):
            v = min(l[i], r[i]) - h
            # 忘了这一步，当是负数时，就表示只能接 0 的雨水
            s += max(0, v)
        return s
        
# @lc code=end

