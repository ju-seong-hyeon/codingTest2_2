def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

if __name__ == "__main__":
    n, m = map(int, input().split())
    ch = [[0] * m for _ in range(n)]
    x, y, dir = map(int, input().split())
    ch[x][y] = 1

    a = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    cnt = 1
    turn_time = 0

    while True:
        turn_left()
        nx = x + dx[dir]
        ny = y + dy[dir]

        if(ch[nx][ny] == 0 and a[nx][ny] ==0):
            ch[nx][ny] = 1
            x = nx
            y = ny
            cnt += 1
            turn_time = 0
            continue
        else:
            turn_time += 1
        if(turn_time == 4):
            nx = x - dx[dir]
            ny = y - dy[dir]
            if a[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0
    print(cnt)
