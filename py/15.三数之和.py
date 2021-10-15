# encoding: utf-8
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    # 时间复杂度为 N^2
    # 主要有两点需要注意的
    # 第一个是连数，第二个是答案去重，但是可以通过先对数组进行排序来解决
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        num_dict = {}
        for i, e in enumerate(nums[:-2]):
            # 如果遇到连数，则不检查跳过
            if i >= 1 and e == nums[i - 1]: continue
            for v in nums[i+1:]:
                if e not in num_dict:
                    num_dict[-v-e] = 1
                else:
                    res.append((e, v, -v-e))
        return res

        
# @lc code=end

