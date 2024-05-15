#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        l=len(x)
        count=0
        for i in range(l):
            if x[i]==x[l-i-1]:
                count+=1
            else:
                return False
                break
        return True
        
# @lc code=end

