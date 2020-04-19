# Given a m x n grid filled with non-negative numbers,
#  find a path from top left to bottom
#  right which minimizes the sum of all numbers along its path.
n = int(input("row size"))
m = int(input("col size"))

a = []
for i in range(0,n):
    b = []
    for j in range(0,m):
        b.append(int(input()))
    a.append(b)
print(a)

for i in range(1,m):
    a[0][i]=a[0][i]+a[0][i-1]
print(a)
for i in range(1,n)    :
    a[i][0] = a[i][0]+a[i-1][0]
print(a)
for i in range(1,n)    :
    for j in range(1,m):
        print(min(a[i-1][j],a[i][j-1]))
        a[i][j] = a[i][j]+min(a[i-1][j],a[i][j-1])

print(a[-1][-1])
