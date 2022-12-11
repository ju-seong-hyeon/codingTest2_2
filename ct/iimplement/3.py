dx = [-1, -1, -2, -2, 1, 1, 2, 2]
dy = [2, -2, -1, 1, -2, 2, 1, -1]


if __name__ == "__main__":
    cur = input()
    x = cur[0]
    x = ord(x) - 97
    y = int(cur[1]) - 1
    # print(x)
    # # cur = list(map(int, cur))
    # print(cur)
    cnt = 0
    arr = [[0] * 8 for _ in range(8)]
    for i in range(8):
        xx = x + dx[i]
        yy = y + dy[i]
        if(0<=xx<8 and 0<=yy<8):
            cnt += 1
    print(cnt)