class SnapshotArray:

    def __init__(self, length: int):
        self.curr = {i:[[0,0]] for i in range(length)}
        self.snap_count = 0

    def set(self, index: int, val: int) -> None:
        self.curr[index].append([self.snap_count, val])

    def snap(self) -> int:
        self.snap_count +=1
        return self.snap_count -1

    def get(self, index: int, snap_id: int) -> int:

        for i in range(len(self.curr[index]) - 1, -1, -1):

            if self.curr[index][i][0] <= snap_id:

                return self.curr[index][i][1]