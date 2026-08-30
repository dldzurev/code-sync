class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_end_time = []
        fleets = len(position) 
        for pos,spd in sorted(zip(position, speed), reverse=True):
            targ_time = (target - pos)/spd
            if pos_end_time and targ_time <= pos_end_time[-1][1]:
                fleets -= 1
                continue
            pos_end_time.append((pos, targ_time))
        return fleets