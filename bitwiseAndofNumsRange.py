# Given a range [m, n] where 0 <= m <= n <= 2147483647,
#  return the bitwise AND of all numbers in this range, inclusive.


m = int(input("enter the left num"))
n = int(input("enter the right num"))

count = 0
while m<n:
    m = m>>1
    n = n>>1
    count = count+1
return m<<count
