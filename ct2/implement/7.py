def dfs(lev, rot):
    global a_min
    if(lev == m):
        print(tmp)
        # for i in home:
        #     dis = 0
        #     h_x, h_y = i[0], i[1]
        #     for j in tmp:
        #         ck_x, ck_y = ck[j[0]][j[1]]
        #         v = abs(h_x - ck_x) + abs(h_y - ck_y)
        #         dis = min(dis, v)
        #     a_min = min(dis, a_min)
        #
        # tmp.clear()
    else:
        for i in range(rot, m):
            tmp.append(ck[i])
            dfs(lev+1, rot+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ck = []
    home = []
    a_min = 100000
    for i in range(n):
        for j in range(n):
            if(a[i][j] == 2):
                ck.append((i, j))
            if(a[i][j] == 1):
                home.append((i, j))

    tmp = []
    dfs(0, 0)
    # print(tmp)
    print(a_min)

