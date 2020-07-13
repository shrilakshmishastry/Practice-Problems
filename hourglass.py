# Function Description
#
# Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in the array.
#
# hourglassSum has the following parameter(s):
#
#     arr: an array of integers

mat = [list(map(int,input().strip(" ").split(" ")))for i in range(6)]

arr = []
for i in range(0,4):

    Sum = 0

    for m in range(0,4):
        Sum =0
        Sum = Sum+mat[i+1][m+1]


        for j in range(m,m+3,1):
            Sum = Sum+mat[i][j]
            Sum = Sum+mat[i+2][j]


        arr.append(Sum)


print(max(arr))
