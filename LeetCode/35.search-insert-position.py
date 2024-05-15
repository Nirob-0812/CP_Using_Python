#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        try:
            return nums.index(target)
        except ValueError:
            nums.append(target)
            nums=sorted(nums)
            return nums.index(target)
        
# @lc code=end

