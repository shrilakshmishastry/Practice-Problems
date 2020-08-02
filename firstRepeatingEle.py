# Given an integer array.
# The task is to find the first repeating element in
#  the array i.e., an element that occurs more than once
#  and whose index of first occurrence is smallest.
t = int(input())
for k in range(0,t):
    n = int(input())
    l = list(map(int,input().strip().split()))
    d = dict()
    for i in l:
        d[i] = d.get(i,0)+1
    print(d)    
    val = list(d.values())
    print(val)
    if max(val)     == 1:

        print(-1)
    else:
        print(val.index(max(val))+1)
