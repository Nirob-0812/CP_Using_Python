#
# @lc app=leetcode id=2859 lang=python
#
# [2859] Sum of Values at Indices With K Set Bits
#

# @lc code=start
class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        s=sum(nums[i]  for i in range(len(nums)) if bin(i)[2:].count('1')==k )
        return s
        
# @lc code=end

