#
# @lc app=leetcode id=1790 lang=python3
#
# [1790] Check if One String Swap Can Make Strings Equal
#


# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if s1 == s2:
            return True

        diffIndices = []

        for i, char in enumerate(s1):

            if not char == s2[i]:
                diffIndices.append(i)

        if len(diffIndices) > 2:
            return False

        swap = (
            s1[: min(diffIndices)]
            + s1[max(diffIndices)]
            + s1[min(diffIndices) + 1 : max(diffIndices)]
            + s1[min(diffIndices)]
            + s1[max(diffIndices) + 1 :]
        )

        if swap == s2:
            return True

        return False


# @lc code=end
