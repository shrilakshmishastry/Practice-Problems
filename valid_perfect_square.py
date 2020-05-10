# Given a positive integer num,
#  write a function which
#   returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0 or num==1:
            return True
        start =0
        end  = num//2
        print(start,end,num)

        while(start<=end):
            mid=(start+end)//2
            print(mid)
            if(mid*mid == num):
                return True
            elif(mid*mid <num):
                start = mid+1
            else:
                end = mid-1
        return False
