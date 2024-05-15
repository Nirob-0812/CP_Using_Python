#
# @lc app=leetcode id=2114 lang=python
#
# [2114] Maximum Number of Words Found in Sentences
#

# @lc code=start
class Solution(object):
    def mostWordsFound(self, sentences):
        m=max(len(i.split()) for i in sentences)
        return m
        
# @lc code=end

