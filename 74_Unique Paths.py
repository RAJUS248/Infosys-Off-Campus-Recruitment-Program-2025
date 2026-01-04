def uniquePaths(m, n):

    arr = []
    for r in range(m):
        row = []
        for c in range(n):

            if r == 0 or c == 0:
                row.append(1)
            else:
                row.append(0)

        arr.append(row)
        
    for r in range(1,m):
        for c in range(1,n):

            arr[r][c] = arr[r-1][c] + arr[r][c-1]

    return arr[m-1][n-1]


m = 3
n = 2
print(uniquePaths(m,n))


def uniquePaths_v1(m: int, n: int) -> int:
    dp = [1] * n
    
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j-1]
    
    return dp[-1]

m = 3
n = 7
print(uniquePaths_v1(m,n))


def uniquePaths_v2(m: int, n: int) -> int:
    dp = []

    for _ in range(m):
        dp.append([1] * n)

    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1],dp
m = 3
n = 7
print(uniquePaths_v2(m,n))
