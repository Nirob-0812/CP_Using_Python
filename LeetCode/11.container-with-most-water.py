#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        m_a=0
        l=0
        r=len(height)-1
        while l<r:
            a=min(height[l],height[r])*(r-l)
            m_a=max(a,m_a)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return m_a
        
# @lc code=end

