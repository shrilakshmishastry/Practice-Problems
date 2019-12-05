# You start with an array A of size N.
#  Also, A[i] = 0 for i = 1 to N. You will be given K positive integers.
#   Let j be one of these integers, you have to add 1 to all A[i], for i >= j.
# Your task is to print the array A after all these K updates are done.
t = int(input())
for i in range(0,t):
    n,k = input().split()
    n = int(n)
    k = int(k)
    array = map(int,input().strip().split())
    array = list(array)
    List = [0]*n
    iterator = iter(array)

    for j in array:
        for m in range(j-1,n):
            List[m]=List[m]+1

    print(*List)
