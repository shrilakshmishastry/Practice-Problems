# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as
#  you like (i.e., buy one and sell one share of the stock multiple times).
#
# Note: You may not engage in multiple transactions at the same
# time (i.e., you must sell the stock before you buy again).
from itertools import permutations
l = map(int,input().strip("" ).split())
l = list(l)
print(l)


prevsum = 0
for i in range(0,len(l)-1):
    for k in range(1,len(l)-i):
        print("k",k)
        mainsum = l[i+k]-l[i]
        print("i",i)
        print("l[i]",l[i])
        print("mainsum",mainsum)
        if (mainsum>prevsum):
            prevsum = mainsum

        com =     permutations(l[i+k+1:len(l)], 2)

        for j in list(com):
            print(j[1],j[0])
            sum = mainsum+(j[1]-j[0])
            print("sum",sum)
            if(sum > prevsum):
                prevsum = sum

print(prevsum)
