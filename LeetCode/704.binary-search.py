#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        left=0
        right=len(nums)-1
        b=False
        while left<=right:
            mid=(right+left)//2
            if nums[mid]==target:
                b=True
                break
            elif nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
        if b:
            return mid
        else:
            return -1
        
# @lc code=end

