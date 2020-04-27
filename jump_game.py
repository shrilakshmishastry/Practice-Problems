# Given an array of non-negative integers, you are initially
#  positioned at the first index of the array.
#
# Each element in the array represents your maximum
# jump length at that position.
#
# Determine if you are able to reach the last index.
l = list(map(int,input().strip().split()))
print(l)

maxReach =0

for i in range(len(nums)):
    if(i>maxReach):
        print( False)
    maxReach = max(maxReach,i+l[i])
print(True)
