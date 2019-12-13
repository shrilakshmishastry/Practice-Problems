# Given an array A[]  of n elements. 
# Your task is to complete the Function num which
#  returns an integer denoting the total number of
#  times digit k appears in the whole array.
t = int(input())
for i in range(0,t):
    size = int(input())
    arr = map(int,input().strip().split())
    # number to be find
    k =input()
    arr = list(arr)
    arr = ' '.join(map(str,arr))
    print(arr.count(k))
