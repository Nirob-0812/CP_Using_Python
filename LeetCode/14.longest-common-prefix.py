#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        min_s=min(strs,key=len)
        for i,char in enumerate(min_s):
            if any(s[i]!=char for s in strs):
                common_s=min_s[:i]
                break
        else:
            common_s=min_s
        return common_s
        
# @lc code=end

