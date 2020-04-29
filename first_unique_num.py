# You have a queue of integers, you need to retrieve
#  the first unique integer in the queue.
#
# Implement the FirstUnique class:
#
#     1.FirstUnique(int[] nums) Initializes the object
#        with the numbers in the queue.
#     2.int showFirstUnique() returns the value of the
#       first unique integer of the queue, and returns -1
#        if there is no such integer.
#     3.void add(int value) insert value to the queue.

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums

        self.d = dict()
        for i in self.nums:

            self.d[i] = self.d.get(i,0)+1



    def showFirstUnique(self) -> int:
        val = list(self.d.values())
        keys = list(self.d.keys())
        try:
            index = val.index(1)
            return keys[index]
        except:
            return -1


    def add(self, value: int) -> None:
        self.nums.append(value)
        self.d[value] = self.d.get(value,0)+1




# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
