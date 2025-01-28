#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode, cm=-100000000000000) -> int:
        if root == None:
            return 0
        add = 0
        nm = cm
        if root.val >= nm:
            add = 1
            nm = root.val
        leftGood = Solution.goodNodes(self, root.left, nm)
        rightGood = Solution.goodNodes(self, root.right, nm)
        return add + leftGood + rightGood


# @lc code=end
