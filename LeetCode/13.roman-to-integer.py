#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        sum=0
        i=len(s)-1
        while i>=0:
            if (s[i]=='V' and s[i-1]=='I' and i>0):
                sum+=4
                i-=2 
            elif (s[i]=='X' and s[i-1]=='I' and i>0):
                sum+=9
                i-=2
            elif (s[i]=='L' and s[i-1]=='X' and i>0):
                sum+=40
                i-=2
            elif (s[i]=='C' and s[i-1]=='X' and i>0):
                sum+=90
                i-=2
            elif (s[i]=='D' and s[i-1]=='C' and i>0):
                sum+=400
                i-=2
            elif (s[i]=='M' and s[i-1]=='C' and i>0):
                sum+=900
                i-=2
            else:
                if s[i]=="I":
                    sum+=1
                elif s[i]=="V":
                    sum+=5
                elif s[i]=="X":
                    sum+=10
                elif s[i]=="L":
                    sum+=50
                elif s[i]=="C":
                    sum+=100
                elif s[i]=="D":
                    sum+=500
                elif s[i]=="M":
                    sum+=1000
                i-=1

        return sum
        
# @lc code=end

