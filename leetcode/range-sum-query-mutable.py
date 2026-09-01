class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [self.nums[0]]
        for i in range(1,len(nums)):
            self.prefix.append(self.prefix[-1] + nums[i])
        

    def update(self, index: int, val: int) -> None:
        for i in range(index,len(self.nums)):
            self.prefix[i] = self.prefix[i] + val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        if (left == 0):
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)