# Given an array with repeated elements,
# the task is to find the maximum distance between
# two occurrences of an element.
t  = int(input())
#nuber of test case
for i in range(0,t):
    size = int(input())
    arr = map(int,input().strip().split())
    arr = list(arr)
    max =0
    for i in arr:
        c = len(arr) - arr[::-1].index(i)-1
        c = c-arr.index(i)
        if(c>max):
            max=c
    print(max)
