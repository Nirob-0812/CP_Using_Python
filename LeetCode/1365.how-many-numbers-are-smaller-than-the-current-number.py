#
# @lc app=leetcode id=1365 lang=python
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        s=[sum(nums[i]>nums[j] for j in range(len(nums))) for i in range(len(nums))]
        
        return s
        
# @lc code=end

