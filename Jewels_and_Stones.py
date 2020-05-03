# You're given strings J representing the types of stones
#  that are jewels, and S representing the stones you have.
#  Each character in S is a type of stone you have.
#  You want to know how many of the stones you have are also jewels.
#
# The letters in J are guaranteed distinct, and all
#  characters in J and S are letters.
#   Letters are case sensitive, so "a" is
#    considered a different type of stone from "A".
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # using dict to get the count
        d = dict()
        for i in range(0,len(J)):

            d[J[i]] = 0


        for i in range(0,len(S)):
            if(S[i] in d):
                d[S[i]]=d.get(S[i],0)+1

        keys = list(d.values())

        return sum(keys)
