class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])#sort logs by ascending time stamp
        servers = {}
        answers = {}
        left = 0
        right = 0

        for q in sorted(queries):

            # Add all requests up to time q
            while right < len(logs) and logs[right][1] <= q:
                server, time = logs[right]
                servers[server] = servers.get(server, 0) + 1
                right += 1

            # Remove requests that are too old
            while left < right and logs[left][1] < q - x:
                server, time = logs[left]
                servers[server] -= 1

                if servers[server] == 0:
                    del servers[server]

                left += 1

            answers[q] = n - len(servers)

        return [answers[q] for q in queries]