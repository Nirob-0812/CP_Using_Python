#
# @lc app=leetcode id=2798 lang=python
#
# [2798] Number of Employees Who Met the Target
#

# @lc code=start
class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        k=1
        s=sum(k for i in hours if i>=target)
        return s
        
# @lc code=end

