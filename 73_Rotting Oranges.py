from collections import deque
def orangesRotting(grid):

    row,col = len(grid),len(grid[0])
    fresh = 0
    q = deque()

    for r in range(row):
        for c in range(col):

            if grid[r][c] == 2:
                q.append((r,c))

            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0
    
    minutes = 0
    direction = [(0,1),(0,-1),(1,0),(-1,0)]

    while q and fresh > 0:
        minutes += 1

        for _ in range(len(q)):
            r,c = q.popleft()

            for dr,dc in direction:
                nr,nc = r + dr, c + dc

                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr,nc))


    return minutes if fresh == 0 else -1


grid = [[2,1,1],[1,1,0],[2,1,1]]

print(orangesRotting(grid))