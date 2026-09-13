from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(starts):
            visited = set(starts)
            queue = deque(starts)

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            return visited

        pacific_starts = []
        atlantic_starts = []

        for r in range(rows):
            pacific_starts.append((r, 0))
            atlantic_starts.append((r, cols - 1))

        for c in range(cols):
            pacific_starts.append((0, c))
            atlantic_starts.append((rows - 1, c))

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        return [
            [r, c]
            for r in range(rows)
            for c in range(cols)
            if (r, c) in pacific and (r, c) in atlantic
        ]