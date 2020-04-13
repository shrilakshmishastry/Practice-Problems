# We have a collection of stones, 
# each stone has a positive integer weight.
#
# Each turn, we choose the two heaviest stones
# and smash them together.  Suppose the stones
# have weights x and y with x <= y.  The result of this smash is:
#
#     If x == y, both stones are totally destroyed;
#     If x != y, the stone of weight x is totally
#      destroyed, and the stone of weight y has new weight y-x.
#
# At the end, there is at most 1 stone left.
# Return the weight of this stone (or 0 if there are no stones left.)

l1 = map(int,input().strip().split())
l1 = list(l1)
print(l1)
l1.sort()
i = len(l1)-1
while len(l1)>1:
    diff = l1[i]-l1[i-1]
    l1[i]=diff
    l1.remove(l1[i-1])
    l1.sort()
    i=i-1
print(l1[0])
