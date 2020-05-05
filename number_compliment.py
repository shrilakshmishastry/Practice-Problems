# Given a positive integer, output its complement number. 
# The complement strategy is to flip the bits of its binary
# representation.

class Solution:
    def findComplement(self, num: int) -> int:
        print(bin(num).replace("0b",""))

        n1 = list(bin(num).replace("0b",""))
        print(n1)
        for i in range(0,len(n1)):
            if(n1[i]=='1'):
                n1[i]="0"
            else:
                n1[i]="1"
        n2 = "".join(n1)
        print(int(n2,2))
        return int(n2,2)
