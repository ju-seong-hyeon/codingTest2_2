def dfs(lev, tot):
    if(lev == n):
        # b.add(tot)
        c[tot] = 1
        return
    else:
        # b.add(a[lev])
        c[a[lev]] = 1
        dfs(lev+1, tot+a[lev])
        dfs(lev+1, tot)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * (sum(a)+1)
    b = set()
    dfs(0, 0)
    print(b)
    print(c)

    for i in range(1, sum(a)+1):
        if c[i] == 0:
            print(i)
            break