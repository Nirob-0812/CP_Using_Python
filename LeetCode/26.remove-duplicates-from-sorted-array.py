#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        length=len(nums)
        k=1
        if length==0 or length==1:
            return length
        else:
            for i in range(length-1):
                if nums[i]!=nums[i+1]:
                    nums[k]=nums[i+1]
                    k+=1
            return k

        
# @lc code=end

