#
# @lc app=leetcode id=2011 lang=python
#
# [2011] Final Value of Variable After Performing Operations
#

# @lc code=start
class Solution(object):
    def finalValueAfterOperations(self, operations):
        p,n=0,0
        for i in operations:
            if i[1]=='+':
                p+=1
            else:
                n+=1
        return p-n
        
# @lc code=end

