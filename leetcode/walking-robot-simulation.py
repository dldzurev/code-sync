class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        #start at 0,0 facing north
        #-2 -> lef 90
        #-1-> right 90
        #1<=k<= move forwar k units 1 at a timee
                    #x,y
        max_dist = 0
        curr = [0,0]
        directions = [(0, 1),   # 0 = North
                    (1, 0),   # 1 = East
                    (0, -1),  # 2 = South
                    (-1, 0)   ]
        direction_index = 0
        obst = {(x,y) for x,y in obstacles}
        for index,command in enumerate(commands):
            if(command == -2):
                direction_index = (direction_index - 1) % 4
            elif(command == -1):
                direction_index = (direction_index + 1) % 4
            else:
                for i in range(command):
                    next_pos = (curr[0] + directions[direction_index][0],curr[1] + directions[direction_index][1])
                    if next_pos in obst:
                        break
                    curr_dist = next_pos[0] * next_pos[0] + next_pos[1] * next_pos[1]
                    max_dist = max(curr_dist,max_dist)
                    curr = next_pos
        return max_dist