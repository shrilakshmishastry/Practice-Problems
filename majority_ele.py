# Given an array of size n, find the majority element.
#  The majority element is the element that appears
#   more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty
# and the majority element always exist in the array.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            d[i]=d.get(i,0)+1
        # print(d)
        # value = list(d.values())
        for i in d:
            if d[i] > (len(nums)//2):
                return i
        return None
