#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:

        for y,row in enumerate(board):
            
            if y==0 or y==len(board)-1:
                edgeFlag = True
            else:
                edgeFlag = False

            for x,col in enumerate(row):
                
                #Edge check
                if x==0 or x==len(row)-1:
                    edgeFlag = True

                if y>0 and x>0:
                    

                



        """
        Do not return anything, modify board in-place instead.
        """
        
# @lc code=end

