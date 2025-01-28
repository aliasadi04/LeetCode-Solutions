#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):

        if list1 == None:
            return list2

        if list2 == None:
            return list1

        if list1.val < list2.val:
            mergedList = ListNode(self, list1.val)
            list1 = list1.next
        else:
            mergedList = ListNode(self, list2.val)
            list2 = list2.next

        returnList = mergedList

        while not (list1 == None or list2 == None):
            if list1.val < list2.val:
                mergedList.next = ListNode(self, list1.val)
                list1 = list1.next
            else:
                mergedList.next = ListNode(self, list2.val)
                list2 = list2.next

            mergedList = mergedList.next

        if list1 == None:
            addRestList = list2
        if list2 == None:
            addRestList = list1

        while not addRestList == None:
            mergedList.next = ListNode(self, addRestList.val)

            addRestList = addRestList.next

            mergedList = mergedList.next

        return returnList


# @lc code=end
