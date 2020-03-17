#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
from copy import deepcopy
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # ref: https://blog.csdn.net/qq_17550379/article/details/82933187

        strl = len(s)
        mem = [False] * (strl + 1)
        mem[0] = True
        for i in range(0, strl + 1):
            
            for word in wordDict:
                if i >= len(word) and mem[i - len(word)] \
                    and word == s[i-len(word):i]:
                    mem[i] = True
                    break
        
        return mem[-1]
        
# @lc code=end

