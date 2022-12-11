dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if(0<=xx<n and 0<=yy<m and a[xx][yy] == 0):
            a[xx][yy] = 1
            dfs(xx, yy)

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [list(map(int, input())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if(a[i][j] == 0):
                dfs(i, j)
                cnt += 1
    print(cnt)