# Given an array with n distinct elements, 
# convert the given array to a reduced form where all
#  elements are in range from 0 to n-1.
#  The order of elements is same, i.e.,
#  0 is placed in place of smallest element,
#   1 is placed for second smallest element,
# … n-1 is placed for largest element.
import copy
t = int(input())
for k in range(0,t):
    n = int(input())
    l = list(map(int,input().strip().split()))
    m = copy.deepcopy(l)
    m.sort()
    b = []
    for i in l:
        index = m.index(i)
        b.append(index)
    print(*b)
