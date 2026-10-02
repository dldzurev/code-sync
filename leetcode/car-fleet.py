class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [[p,s] for p,s in zip(position,speed)]
        stack = []
        for pos,spd in sorted(pos_speed)[::-1]:
            finish_time =  (target - pos)/spd
            stack.append(finish_time)
            if(len(stack) > 1 and stack[-1] <= stack[-2]):
                stack.pop()
        return len(stack)