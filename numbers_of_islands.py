# Given a 2d grid map of '1's (land) and '0's (water),
# count the number of islands. An island is surrounded by water and
#  is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
def bfs(i,j)            :
    if (i<0 or j<0 or i>=len(a) or j>=len(a[i]) or a[i][j] == 0):
        return ;
    a[i][j]=0
    bfs(i+1,j)
    bfs(i-1,j)
    bfs(i,j+1)
    bfs(i,j-1)

n = int(input("enter the size of row"))
m = int(input("enter the size of column"))
a = list()
print(a)
for i in range(0,n):
    b = []
    for j in range(0,m):
        b.append(int(input()))
    a.append(b)

print(a)
count = 0
for i in range(0,n):
    for j in range(0,m):
        if a[i][j] == 1:
            count = count+1
            bfs(i,j)
print(count)
