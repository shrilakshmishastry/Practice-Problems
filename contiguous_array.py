# Given a binary array, 
# find the maximum length of a contiguous
# subarray with equal number of 0 and 1.
l = map(int,input().strip().split())
l = list(l)

d = dict()
d[0]=-1
count = 0
maxlen =0
for i in range(0,len(l)):
    if(l[i]==0):
        count = count-1
    else:
        count = count+1
    if (count in d):
        maxlen = max(maxlen,i-d[count])
    else:
        d[count]    = i

print(maxlen)
