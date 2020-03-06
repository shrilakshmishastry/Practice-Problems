# Given a matrix mat[] of size n x m, where every row and
#  column is sorted in increasing order, and a number x is given.
# The task is to find whether element x is present in the matrix or not.

t = int(input())
for i in range(0,t):
    m,n = map(int,input().strip().split())
    arr = map(int,input().strip().split())
    arr = list(arr)
    k = int(input())
    if(arr.count(k)>=1):
        print(1)
    else:
        print(0)
