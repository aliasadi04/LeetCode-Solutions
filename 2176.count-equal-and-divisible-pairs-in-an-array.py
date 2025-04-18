#
# @lc app=leetcode id=2176 lang=python3
#
# [2176] Count Equal and Divisible Pairs in an Array
#


# @lc code=start
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        c = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i * j % k == 0 and nums[i] == nums[j]:
                    c += 1
        return c


# @lc code=end
