#
# @lc app=leetcode id=2248 lang=python
#
# [2248] Intersection of Multiple Arrays
#

# @lc code=start
class Solution(object):
    def intersection(self, nums):
        arr=[]
        b=False
        for i in nums[0]:
            for j in nums:
                if i not in j:
                    b=False
                    break
                else:
                    b=True
            if b:
                arr.append(i)
        return sorted(arr)

        
# @lc code=end

