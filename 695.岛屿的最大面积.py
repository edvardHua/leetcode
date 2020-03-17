#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:

    def _dfs(self, row_id, col_id):
        # terminator
        if row_id >= self.height or col_id >= self.width \
            or row_id < 0 or col_id < 0:
            return 0
        
        if self.visited[row_id][col_id] or self.grid[row_id][col_id] == 0:
            return 0

        direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        self.visited[row_id][col_id] = 1
        # mean can reach, therefore plus one
        ans = 1
        for rd, cd in direction:
            ans += self._dfs(row_id + rd, col_id + cd)
        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.height, self.width = len(grid), len(grid[0])
        self.visited = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.grid = grid

        max_val = 0
        for r in range(self.height):
            for c in range(self.width):
                v = self._dfs(r, c)
                max_val = max(v, max_val)
        
        return max_val

        
# @lc code=end

