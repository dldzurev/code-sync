class Solution:
    def maxArea(self, height: List[int]) -> int:
        curr_max, L = 0, 0
        R = len(height) - 1
        while(L < R):
            vol = min(height[L],height[R]) * (R - L)
            if(vol > curr_max): curr_max = vol
            if((height[L] * (R - L)) <= curr_max): L += 1
            if((height[R] * (R - L)) <= curr_max): R -= 1
        return curr_max