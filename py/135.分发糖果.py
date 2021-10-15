#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 1. 暴力法，因为每个学生至少可以获得一个糖果
        # 因此，我们可以不断遍历，当糖果数目不再发生变化的时候，这个时候即为需要准备的糖果数
        # 2. 因为这里分别比较左边的元素是否比右边小，再分别比较右边元素是否比左边小，然后
        # 取一个最大值再 sum 即可
        if not ratings: return 0

        rl = len(ratings)

        l2r, r2l = [1 for _ in range(rl)], [1 for _ in range(rl)]

        for i in range(1, rl):
            if ratings[i] > ratings[i-1]:
                l2r[i] = l2r[i-1] + 1
        
        for i in range(rl - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                r2l[i] = r2l[i+1] + 1
        
        ans = 0
        for i in range(0, rl):
            ans += max(l2r[i], r2l[i])
        
        return ans
        

# @lc code=end

