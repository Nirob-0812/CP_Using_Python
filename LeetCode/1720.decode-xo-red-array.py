#
# @lc app=leetcode id=1720 lang=python
#
# [1720] Decode XORed Array
#

# @lc code=start
class Solution(object):
    def decode(self, encoded, first):
        x=[]
        x.append(first)
        for i in range(len(encoded)):
            x.append(x[i]^encoded[i])
        return x
        
# @lc code=end

