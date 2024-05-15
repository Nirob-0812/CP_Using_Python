#
# @lc app=leetcode id=2974 lang=python
#
# [2974] Minimum Number Game
#

# @lc code=start
class Solution(object):
    def numberGame(self, nums):
        a=[]
        srt=sorted(nums)
        for i in range(0,len(nums),2):
            a.append(srt[i+1])
            a.append(srt[i])
        return a
# @lc code=end

