def dfs(lev, tot):
    global a_sum
    if(lev == n):
        a_sum = max(a_sum, tot)
    else:
        dfs(lev+1, tot*a[lev])
        dfs(lev+1, tot+a[lev])

if __name__ == "__main__":
    a = list(map(int, input()))
    n = len(a)
    a_sum = 0
    dfs(0, 0)
    print(a_sum)

