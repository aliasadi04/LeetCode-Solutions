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
        initDeletions = s.count("a")
        deletionsList = [initDeletions]

        for char in s:
            deletionsList.append(deletionsList[-1] + (1 if char == "b" else -1))

        return min(deletionsList)


# @lc code=end
