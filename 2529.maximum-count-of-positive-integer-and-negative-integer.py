#
# @lc app=leetcode id=2529 lang=python3
#
# [2529] Maximum Count of Positive Integer and Negative Integer
#

# @lc code=start
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        numNeg = 0
        for i,num in enumerate(nums):
            
            if num<0:
                numNeg = i + 1
            
                continue
            if num > 0:
                return max(numNeg, len(nums)-i)

                
# @lc code=end

