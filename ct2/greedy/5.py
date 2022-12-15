def dfs(lev, rot):
    global cnt
    if(lev == 2):
        cnt += 1
    else:
        for i in range(rot, n):
            dfs(lev+1, i+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 0
    dfs(0, 0)
    print(cnt)