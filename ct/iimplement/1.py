# dx_r = [0]
# dy_r = [1]
# dx_l = [0]
# dy_l = [-1]
# dx_u = [-1]
# dy_u = [0]
# dx_d = [1]
# dy_d = [0]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

if __name__ == "__main__":
    n = int(input())
    a = list(map(str, input().split()))
    arr = [[0] * n for _ in range(n)]
    cur = [0, 0]
    # print(a)
    for i in a:
        if(i == 'R'):
            xx = dx[0]
            yy = dy[0]
        elif(i == 'L'):
            xx = dx[1]
            yy = dy[1]
        elif(i == 'U'):
            xx = dx[2]
            yy = dy[2]
        else:
            xx = dx[3]
            yy = dy[3]

        x = (cur[0] + xx)
        y = (cur[1] + yy)
        if(0<=x<n and 0<=y<n):
            cur[0] = x
            cur[1] = y

    print(cur[0] + 1, cur[1] + 1)
