#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#


# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        newArr = []
        pointer1 = 0
        pointer2 = 0

        while not (nums1[pointer1] == 0 or pointer2 >= len(nums2)):
            if nums1[pointer1] < nums2[pointer2]:
                newArr.append(nums1[pointer1])
                pointer1 += 1
            else:
                newArr.append(nums2[pointer2])
                pointer2 += 1

        while not pointer2 >= len(nums2):
            newArr.append(nums2[pointer2])
            pointer2 += 1

        while not nums1[pointer1] == 0:
            newArr.append(nums1[pointer1])
            pointer1 += 1
        
        for i in range(len(newArr)):

            nums1[i] = newArr[i]

        """
        Do not return anything, modify nums1 in-place instead.
        """


# @lc code=end
