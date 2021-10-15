#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    # 1. 暴力法，时间复杂度为 N^3
    # 2. 中心扩展法，时间复杂度为 N^2
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def is_palindrome(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l -1
        
        cur = 0
        max_len = 0
        start = 0
        for i in range(n):
            cur = max(is_palindrome(i,i), is_palindrome(i, i + 1))
            if cur > max_len:
                max_len = cur
                start = i - (cur - 1) // 2
        return s[start: start+max_len]

        
# @lc code=end

