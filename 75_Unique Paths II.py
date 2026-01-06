def uniquePathsWithObstacles(obstacleGrid):
    m,n = len(obstacleGrid),len(obstacleGrid[0])

    if obstacleGrid[0][0] == 1:
        return 0
    dp = [0] * n
    dp[0] = 1

    for i in range(m):
        for j in range(n):

            if obstacleGrid[i][j] == 1:
                dp[j] = 0

            elif j > 0:

                dp[j] += dp[j-1]

    return dp[-1]

obstacleGrid = [[0,0,0,0],[0,1,0,0],[0,0,0,0]]
print(uniquePathsWithObstacles(obstacleGrid))


def uniquePathsWithObstacles_v2(obstacleGrid):
    m,n = len(obstacleGrid),len(obstacleGrid[0])

    if obstacleGrid[0][0] == 1:
        return 0
    
    obstacleGrid[0][0] = 1

    for i in range(m):
        for j in range(n):

            if i == 0 and j == 0:
                continue

            if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = 0

            else:
                # If it's empty (0), calculate paths from Top + Left
                up = obstacleGrid[i-1][j] if i > 0 else 0
                left = obstacleGrid[i][j-1] if j > 0 else 0
                obstacleGrid[i][j] = up + left

    return obstacleGrid[m-1][n-1]

obstacleGrid = [[0,0,0,0],[0,1,0,0],[0,0,0,0]]
print(uniquePathsWithObstacles_v2(obstacleGrid))