#
# @lc app=leetcode id=2373 lang=python
#
# [2373] Largest Local Values in a Matrix
#

# @lc code=start
class Solution(object):
    def largestLocal(self, grid):
        m_grid=[]

        for r in range(len(grid)-2):
            new=[]
            for c in range(len(grid[0])-2):
                row=[]
                row.append(sorted((grid[r][c:c+3]),reverse=True))
                row.append(sorted(grid[r+1][c:c+3],reverse=True))
                row.append(sorted(grid[r+2][c:c+3],reverse=True))
                new.append(max(max(row)))
            m_grid.append(new)
        return m_grid
        
# @lc code=end

