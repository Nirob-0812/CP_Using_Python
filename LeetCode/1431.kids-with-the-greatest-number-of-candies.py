#
# @lc app=leetcode id=1431 lang=python
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        m=max(candies)
        return [i+extraCandies>=m for i in candies]
        
# @lc code=end

