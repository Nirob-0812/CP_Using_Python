#
# @lc app=leetcode id=1470 lang=python
#
# [1470] Shuffle the Array
#

# @lc code=start
class Solution(object):
    def shuffle(self, nums, n):
        a=nums[:n]
        b=nums[n:]
        new=[]
        for i in range(n):
            new.append(a[i])
            new.append(b[i])
        
        return new
        
# @lc code=end

