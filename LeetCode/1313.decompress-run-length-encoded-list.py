#
# @lc app=leetcode id=1313 lang=python
#
# [1313] Decompress Run-Length Encoded List
#

# @lc code=start
class Solution(object):
    def decompressRLElist(self, nums):
        l=[nums[i+1] for i in range(0,len(nums),2) for _ in range(nums[i])]
    
        return l
# @lc code=end

