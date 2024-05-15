#
# @lc app=leetcode id=1929 lang=python
#
# [1929] Concatenation of Array
#

# @lc code=start
import numpy as np
class Solution(object):
    def getConcatenation(self, nums):
        ans=np.concatenate((nums,nums))
        return ans
        
# @lc code=end

