#
# @lc app=leetcode id=1672 lang=python
#
# [1672] Richest Customer Wealth
#

# @lc code=start
class Solution(object):
    def maximumWealth(self, accounts):
        return max(sum(i) for i in accounts)
        
# @lc code=end

