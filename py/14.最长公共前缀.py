#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    # 第一种，每扫描到一位都在全部的 list 中匹配，时间复杂度为 O(N)
    # 第二种则是水平扫描，效果比第一种好，时间复杂度也是 O(N)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs): return ""

        comm_prefix = []
        for i, c in enumerate(strs[0]):
            flag = True
            for s in strs[1:]:
                if not i < len(s) or s[i] != c:
                    flag = False
                    break        
            if flag:         
                comm_prefix.append(c)
            else:
                break

        return "".join(comm_prefix)
        
# @lc code=end

