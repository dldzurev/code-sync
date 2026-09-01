class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixes = [nums[0]]
        for i in range(1,len(nums)):
            self.prefixes.append(self.prefixes[i-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixes[right]
        return self.prefixes[right] - self.prefixes[left - 1]