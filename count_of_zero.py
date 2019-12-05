# Given an array of size N consisting of only 0's and 1's ,
# which is sorted in such a manner that all the 1's are
#  placed first and then they are followed by all the 0's.
# You have to find  the count of all the 0's.
t = int(input())
for i in range(0,t):
    size = int(input())
    array = map(int,input().strip().split())
    array = list(array)
    print(array.count(0))
