class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        start = image[sr][sc]#0
        queue = deque()#[0,0]
        if(start == color):
            return image
        queue.append([sr,sc])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        image[sr][sc] = color
        print(image)
        while(queue):
            #print(image)
            r,c = queue.popleft()
            for r_,c_ in directions:
                n_r = r + r_
                n_c = c + c_
                if(0 <= n_r < len(image) and 0 <=n_c <len(image[0]) and image[n_r][n_c] == start):
                    queue.append([n_r,n_c])
                    image[n_r][n_c] = color
        return image