# Given an array nums of n integers where n > 1,  
# return an array output such that output[i]
# is equal to the product of all the elements of nums except nums[i].

l = map(int,input().strip().split())
l = list(l)
print(l)
output = [1]*len(l)
prod = 1

for i in range(len(l)):
    # print(i)
    output[i]*=prod
    prod*=l[i]
prod = 1
for i in range(len(l)-1,-1,-1):
    print(i)
    output[i]*= prod
    prod *=l[i]
    print(output,prod)

print(output)
