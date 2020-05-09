# You are given an array coordinates, 
# coordinates[i] = [x, y], where [x, y] represents
# the coordinate of a point.
# Check if these points make a straight line in the XY plane.
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        c = coordinates
        if len(c)==2:
            return True
        x0,y0=c[0]
        x1,y1=c[1]
        for i in range(2,len(c)):
            x,y=c[i]
            if((y1-y0)*(x-x0))!=((x1-x0)*(y-y0)):
                return False
        return    True
