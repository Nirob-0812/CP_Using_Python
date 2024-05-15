#
# @lc app=leetcode id=3065 lang=python
#
# [3065] Minimum Operations to Exceed Threshold Value I
#

# @lc code=start
class Solution(object):
    def minOperations(self, nums, k):
        return sum(1 for i in nums if i<k)
        
# @lc code=end

