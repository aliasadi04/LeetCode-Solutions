#
# @lc app=leetcode id=1404 lang=python3
#
# [1404] Number of Steps to Reduce a Number in Binary Representation to One
#


# @lc code=start
class Solution:
    def __init__(self):
        self.seenDict = {"1": 0}

    def numSteps(self, si: str) -> int:
        
        if not si in self.seenDict:
            
            s = si

            if s[-1] == "0":
                s = s[:-1]

            else:
                if not "0" in s:
                    s = "1" + "0" * len(s)
                else:
                    s = s[:-1] + "0"
                    index = -2
                    while s[index] == "1":
                        index = index - 1
                    s = s[:index] + "1" + s[index + 1 :]

            nextSteps = self.numSteps(s)
            self.seenDict[si] = nextSteps + 1
            return self.seenDict[si]
        else:
            return self.seenDict[si]


# @lc code=end
