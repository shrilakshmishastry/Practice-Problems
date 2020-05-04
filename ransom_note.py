#  Given an arbitrary ransom note string and another string 
#  containing letters from all the magazines,
#   write a function that will return true if the
#   ransom note can be constructed from the magazines ;
#    otherwise, it will return false.
#
# Each letter in the magazine string can only be used
#  once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = dict()
        d2 = dict()

        for i in range(0,len(ransomNote)):
            d1[ransomNote[i]] = d1.get(ransomNote[i],0)+1

        for j in range(0,len(magazine))    :
            d2[magazine[j]] = d2.get(magazine[j],0)+1
        print(d1,d2)
        for i in d1:
            if i in d2:
                print("true")
                if(d1[i]>d2[i]):
                    return False


            else:
                return False
        return True
