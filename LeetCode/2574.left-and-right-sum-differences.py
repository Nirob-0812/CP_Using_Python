#
# @lc app=leetcode id=2574 lang=python
#
# [2574] Left and Right Sum Differences
#

# @lc code=start
class Solution(object):
    def leftRightDifference(self, nums):
        left=[]
        right=[]
        left.append(0)
        right.append(0)
        for i in range(len(nums)-1):
            left.append(left[i]+nums[i])
        for i in range(len(nums)-1):
            right.append(right[i]+nums[len(nums)-1-i])
        right=right[::-1]
        return [abs(i-j) for i,j in zip(left,right)]
        
# @lc code=end

