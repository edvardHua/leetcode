# -*- coding: utf-8 -*-
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums, target):
        if not nums: return -1

        rotate_ind = 0
        for i, val in enumerate(nums):
            if nums[(i-1) % len(nums)] <= val >= nums[(i+1) % len(nums)]:
                rotate_ind = i
                break
        
        left = right = 0
        # binary search
        if nums[0] <= target <= nums[rotate_ind]:
            left = 0
            right = rotate_ind
        if nums[min(rotate_ind + 1, len(nums) - 1)] <= target <= nums[-1]:
            left = min(rotate_ind + 1, len(nums) - 1)
            right = len(nums) - 1
        
        print(rotate_ind, left, right)

        search_ind = -1
        while right >= left:
            mid = (left + right) // 2
            if nums[mid] == target:
                search_ind = mid
                break

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return search_ind


if __name__ == '__main__':
    s = Solution()
    test = [
        [[4,5,6,7,0,1,2], 0],
        [[4,5,6,7,0,1,2], 3],
        [[3,1], 1],
        [[1], 1]
    ]
    for a, t in test:
        r = s.search(a, t)
        print(r)
        
# @lc code=end

