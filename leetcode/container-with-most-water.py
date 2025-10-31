class Solution:
    def maxArea(self, height: List[int]) -> int:
        ret = 0
        l = 0
        r = len(height) - 1
        while(l<r):
            h = min(height[l],height[r])
            vol = h * (r-l)
            if(vol > ret): ret = vol
            if(height[l] >= height[r]):
                r -= 1
            else:
                l += 1
        return ret