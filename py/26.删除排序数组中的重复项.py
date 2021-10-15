#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    # 其实 python 的话可以直接调用 del 关键字来操作
    # 如果其他语言的话，可以使用双指针，一个快，一个慢
    # 时间复杂度为 N
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 

        # 双指针的办法还是有点巧妙的
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i
        
# @lc code=end

