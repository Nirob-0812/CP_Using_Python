#
# @lc app=leetcode id=1637 lang=python
#
# [1637] Widest Vertical Area Between Two Points Containing No Points
#

# @lc code=start
class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        s=sorted(points)
        h=[]
        for i in range(0,len(s)-1):
            h.append(s[i+1][0]-s[i][0])
        h=sorted(h,reverse=True)
        return h[0]
        
# @lc code=end

