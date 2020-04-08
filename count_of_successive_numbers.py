# Given an integer array arr, count element x such that x + 1 is also in arr.
#
# If there're duplicates in arr, count them seperately.

l = map(int,input().strip().split())
l = list(l)
l.sort()
print(l)
d = dict()

for k in l:
    print("k",k)
    for j in range(0,len(l)):
        print(l[j])
        if (l[j]==(k+1)):
            print("true")
            d[k] = d.get(k,0)+1
            break
print(sum(list(d.values())))
