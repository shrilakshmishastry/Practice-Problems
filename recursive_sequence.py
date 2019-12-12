# A function f is defined as follows F(n)= (1) +(2*3) + (4*5*6) ... n.
# Given an integer n the task is to print the F(n)th term.
# Input:
# The first line of input contains an integer T denoting the number of test cases.
# Then T test cases follow. Each test contains an integer n.
test_case = int(input())
for k in range(0,test_case):
    n = int(input())
    sum =0
    t=1
    for i in range(1,n+1):
        mul=1
        for j in range(t,t+i):
            mul =mul*j
        sum = sum+mul
        t=j+1
    print(sum)
