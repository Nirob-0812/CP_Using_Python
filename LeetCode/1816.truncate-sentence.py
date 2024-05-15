#
# @lc app=leetcode id=1816 lang=python
#
# [1816] Truncate Sentence
#

# @lc code=start
class Solution(object):
    def truncateSentence(self, s, k):
        return ' '.join(s.split()[:k])
        
# @lc code=end

