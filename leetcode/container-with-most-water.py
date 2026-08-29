class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_ = 0

        left = 0
        right = len(height) -1 #3
        x = right - left #2
        max_ = x*min(height[left],height[right]) #3
        while(left<right):
            if (height[left] < height[right]):
                left = left+1
            else:
                right = right-1
            x = right - left#2
            vol = x*min(height[left],height[right])#2*1
            max_ = max(max_,vol)#3
        return max_