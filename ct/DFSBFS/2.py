from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
# def dfs(x, y):
#     global cnt
#     # cnt += 1
#     if(x == n-1 and y == m-1):
#         print(a[x][y])
#         sys.exit(1)
#     else:
#         for i in range(4):
#             xx = x + dx[i]
#             yy = y + dy[i]
#             if(0<=xx<n and 0<=yy<m and a[xx][yy] == 1):
#                 a[xx][yy] = a[x][y] + 1
#                 dfs(xx, yy)

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [list(map(int, input())) for _ in range(n)]
    cnt = 0
    dq = deque()
    dq.append((0, 0))

    while(dq):
        cur = dq.popleft()
        x = cur[0]
        y = cur[1]
        if(x == n-1 and y == m-1):
            print(a[x][y])
            break
        else:
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if(0<=xx<n and 0<=yy<m and a[xx][yy] == 1):
                    a[xx][yy] = a[x][y] + 1
                    dq.append((xx, yy))









