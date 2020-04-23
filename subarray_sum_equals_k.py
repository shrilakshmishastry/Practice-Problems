# Given an array of integers and an integer k,
#  you need to find the total number of continuous
#   subarrays whose sum equals to k.


l = map(int,input("enter list \n").strip().split())
k = int(input("enter sum to be equalize"))
l = list(l)
d = dict()
d[0] = 1

sum =0
count =0
for i in l:
    sum = sum+i

    if sum-k in d    :
        count = count+d[sum-k]
    if sum in d:
        d[sum] = d[sum]+1
    else:
        d[sum]     = 1

print(d,count)
