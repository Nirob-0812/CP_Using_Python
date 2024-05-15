#
# @lc app=leetcode id=1480 lang=python
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution(object):
    def runningSum(self, nums):
        o=[sum(nums[j] for j in range(i+1)) for i in range(len(nums)) ]
        return o
        
# @lc code=end

