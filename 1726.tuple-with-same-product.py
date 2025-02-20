#
# @lc app=leetcode id=1726 lang=python3
#
# [1726] Tuple with Same Product
#


# @lc code=start
class Solution:
    def fact(self,num):
        if num==1:
            return 1
        return self.fact(num-1)*num
    def tupleSameProduct(self, nums) -> int:
        seenDict = {}
        
        for i, num in enumerate(nums):
            for o, num2 in enumerate(nums):

                if i == o:
                    continue

                if num * num2 in seenDict:
                    seenDict[num * num2] = seenDict[num * num2] + 1
                else:
                    seenDict[num * num2] = 1


        sumOfProducts = 0

        for key in seenDict:
            toAdd = int((seenDict[key])/2)

            if toAdd==1:
                continue

            sumOfProducts += self.fact(toAdd)



        return sumOfProducts * 4


# @lc code=end
