def dfs(lev, rot):
    global a_min
    if(lev == m):
        a_sum = 0
        for i in tmp:
            ck_x = ck[i][0]
            ck_y = ck[i][1]
            dis = 2147000000
            for j in hm:
                hm_x = j[0]
                hm_y = j[1]
                # print(ck_x, ck_y, hm_x, hm_y)
                dis = min(dis, (abs(ck_x - hm_x) + abs(ck_y - hm_y)))
            a_sum += dis
            # print(a_sum)
        a_min = min(a_sum, a_min)
    else:
        for i in range(rot, len(ck)):
            tmp[lev] = i
            dfs(lev+1, i+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    hm = []
    ck = []
    a_min = 2147000000
    for i in range(n):
        for j in range(n):
            if(a[i][j] == 1):
                hm.append((i, j))
            elif(a[i][j] == 2):
                ck.append((i, j))

    tmp = [0] * m
    dfs(0, 0)
    print(a_min)