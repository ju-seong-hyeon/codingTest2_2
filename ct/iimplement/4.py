dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# dx_n = [-1]
# dy_n = [0]
# dx_e = [0]
# dy_e = [1]
# dx_s = [1]
# dy_s = [0]
# dx_w = [0]
# dy_w = [-1]

dic = {0 : [-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]}

def dir_change(v):
    if(v < 4):
        v += 1
    else:
        v = 0
    return v

if __name__ == "__main__":
    n, m = map(int, input().split())
    cur = list(map(int,input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    ch = [[0] * m for _ in range(n)]
    # dir = [0, 1, 2, 3]
    cnt = 1
    ch[cur[0]][cur[1]] = 1

    cur_dir = cur[2]
    cur_lo = [cur[0], cur[1]]

    while(True):
        dir = dic[cur_dir]
        xx = cur_lo[0] + dir[0]
        yy = cur_lo[1] + dir[1]

        if(0<=xx<n and 0<=yy<n and arr[xx][yy] == 0):
            if(ch[xx][yy] == 0):
                ch[xx][yy] = 1
                cur_lo = [cur[xx][yy]]

            # else:
        elif(0<=xx<n and 0<=yy<n and arr[xx][yy] == 1):
            cur_dir = dir_change(cur_dir)








