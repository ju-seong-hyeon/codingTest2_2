dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
dic = {0 : [-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]}

if __name__ == "__main__":
    n, m = map(int, input().split())
    cur = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ch = [[0] * m for _ in range(n)]

    ch[cur[0]][cur[1]] = 1
    cnt = 1
    dir = cur[2]
    loc = [cur[0], cur[1]]
    while(True):
        x = loc[0] + dir[0]
        y = loc[1] + dir[1]

        if(0<=x<n and 0<=y<m and a[x][y] == 0):
            if(ch[x][y] == 0):
                loc = [x, y]
            else:
                dir += 1
                if(dir== 4):
                    dir = 0
        elif(0<=x<n and 0<-y<m and a[x][y] == 1):
            dir += 1
            if(dir == 4):
                dir = 0
