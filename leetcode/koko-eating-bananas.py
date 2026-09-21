class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1, max(piles)
        min_speed = r
        while(l<=r):
            k = (l+r)//2
            curr_h = 0
            for pile in piles:
                curr_h += math.ceil(pile / k)
            if curr_h <= h:
                min_speed = min(min_speed,k)
                r = k-1
            else:
                l = k+1
        return min_speed