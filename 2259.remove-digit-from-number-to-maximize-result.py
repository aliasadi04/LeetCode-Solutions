#
# @lc app=leetcode id=2259 lang=python3
#
# [2259] Remove Digit From Number to Maximize Result
#


# @lc code=start
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        currentHighest = 0
        for i, num in enumerate(number):
            if num == digit:
                if int(number[:i] + number[i + 1 :]) > int(currentHighest):
                    currentHighest = number[:i] + number[i + 1 :]
        return currentHighest


# @lc code=end
