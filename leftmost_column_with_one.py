 # """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n,m = binaryMatrix.dimensions()

        current_row = 0
        currentcol = m-1
        while(current_row <=n-1 and currentcol>=0):
            if(binaryMatrix.get(current_row,currentcol) == 0):
                current_row = current_row+1
            else   :
                currentcol-=1
        if        currentcol !=m-1:
            return currentcol+1
        else :
            return -1
