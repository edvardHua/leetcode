#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    # 这题使用动态规划求解会简单点
    # 如果是分治，繁琐一点，复杂度也不是最优
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0

        # 动态规划，如果加上当前值，ans 为负数的话，则没有增益效果
        # 代码直接，但需要一定推理能力
        ans = sum = nums[0]
        for n in nums[1:]:
            if sum > 0:
                sum += n
            else:
                sum = n
            
            ans = max(sum, ans)
            
        return ans
        
# @lc code=end

