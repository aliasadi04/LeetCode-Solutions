#
# @lc app=leetcode id=1653 lang=python3
#
# [1653] Minimum Deletions to Make String Balanced
#


# @lc code=start
class Solution:
    def minimumDeletions(self, s: str) -> int:
        if len(s) == 1 or s.count("a") == 0 or s.count("b") == 0:
            return 0
        
        currentMin = 10000000000000
        
        for i in range(len(s)+1):

            count = s[:i].count("b") + s[i:].count("a")
            if count < currentMin:
                currentMin = count
        return currentMin


# @lc code=end
