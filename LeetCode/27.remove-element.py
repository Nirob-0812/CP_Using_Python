#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        length=len(nums)
        k=0
        for i in range(length):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k
        
# @lc code=end

