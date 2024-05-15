#
# @lc app=leetcode id=1351 lang=python
#
# [1351] Count Negative Numbers in a Sorted Matrix
#

# @lc code=start
class Solution(object):
    def countNegatives(self, grid):
        neg=lambda x: x<0
        cnt=sum(neg(i) for r in grid for i in r)
        return cnt
        
# @lc code=end

