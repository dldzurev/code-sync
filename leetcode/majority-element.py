class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counted  = Counter(nums)
        return counted.most_common(1)[0][0]