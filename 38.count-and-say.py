#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#


# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:

        string = str(1)
        for o in range(2, 1 + n):

            newArr = []
            start = 0
            for i, char in enumerate(string):
                if i == len(string) - 1 or char != string[i + 1]:
                    newArr.append(str(i - start + 1) + char)
                    start = i + 1

            string = "".join(newArr)

        return string


# @lc code=end
