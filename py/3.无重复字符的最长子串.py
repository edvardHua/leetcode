#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        seq = set()
        left, cur_len, max_len = 0, 0, 0
        for i in range(len(s)):
            while s[i] in seq:
                seq.remove(s[left])
                left += 1
            
            seq.add(s[i])
            max_len = max(len(seq), max_len)
        
        return max_len
                
# @lc code=end

