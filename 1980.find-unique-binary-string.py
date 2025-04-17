#
# @lc app=leetcode id=1980 lang=python3
#
# [1980] Find Unique Binary String
#


# @lc code=start
import re


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        hash = {}
        for num in nums:
            hash[num] = 1

        start = "1" + "0" * (len(nums[0]) - 1)
        while start in hash:
            string = start

            array = re.split("", string)
            array = array[1:-1]

            index = -1
            while not array[index] == "0":
                index -= 1
            array[index:] = ["0"] * (index * -1)
            array[index] = "1"
            string = "".join(array)
            start = string
        return start


# @lc code=end
