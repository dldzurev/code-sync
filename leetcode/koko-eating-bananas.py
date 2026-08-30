class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k, piles):
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / k)
            return hrs
        prevk1 = max(piles)  # high
        prevk2 = 1           # low
        while prevk2 <= prevk1:
            k = prevk2 + (prevk1 - prevk2) // 2
            if hours_needed(k, piles) <= h:
                prevk1 = k - 1
            else:
                prevk2 = k + 1
        return prevk2