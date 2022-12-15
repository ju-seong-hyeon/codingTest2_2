def dfs(lev):
    if(lev == n+1):
        return
    else:
        b.add(a[lev])
        b.add(sum(b) + a[lev])
        dfs(lev+1)
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = set()
    dfs(0)
    b = list(b)
    b.sort()
    print(b)
    print(b)