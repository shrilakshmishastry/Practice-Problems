# Given an unsorted array arr[] of size N, rotate it by D elements (clockwise). 
test_case = int(input())
for i in range(0,test_case):
    array_size,rotate_pos = input().split()
    array_size = int(array_size)
    rotate_pos  = int(rotate_pos)
    array = map(int,input().strip().split())
    array = list(array)
    temp = array[0:rotate_pos]
    for i in range(rotate_pos,array_size):
        array[i-rotate_pos] = array[i]


    j = 0
    for i in range(array_size-rotate_pos,array_size):
        array[i] = temp[j]
        j=j+1
    print(*array)
