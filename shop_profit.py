# Program to calculate maximum profit and often visit shop in a fait :
#given :
#profit for each shop,number of shops,number of people ,L and R indicating
#the person can visit those shops between inclusively.At a time k people are allowed
from itertools import permutations
t = int(input())
for f in range(0,t):
    n,m= input().split()
    n = int(n)
    m = int(m)
    p = map(int,input().strip().split())
    p = list(p)
    a =[]
    for s in range(0,m):
        arr =[1,2]
        g,h= input().split()
        g = int(g)
        h = int(h)
        arr[0],arr[1] = g,h
        a.append(arr)

    l = list(permutations(range(7),3))

    old_profit = 0
    arr=[]
    for i in l:
        profit = 0
        for j in range(0,3):
            # print(i)
            t = a[i[j]-1]
            # print(t)
            for k in range(t[0]-1,t[1]):

            # print(p[k])
                profit = profit+p[k]
        if(profit>old_profit)    :
            old_profit = profit

    arr =[]
    for k in range(0,len(p)):
        arr.insert(k,0)
    for i in a:

        for j in range(i[0]-1,i[1]):
            arr[j]=arr[j]+1

    print(arr.index(max(arr))+1)
    print(old_profit)
