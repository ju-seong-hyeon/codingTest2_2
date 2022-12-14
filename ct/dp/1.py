from collections import deque
MAX = 30000

def dfs(lev, n):
    if(n == 1):
        return
    elif(n<1):
        return
    else:
        print(n)
        if(n % 5 == 0):
            a[n//5] = min(a[n//5], lev+1)
                a[n//5] = lev + 1
                dfs(lev+1, n/5)
        elif(n % 3 == 0):
            if(a[n//3] > lev + 1):
                a[n // 3] = lev + 1
                dfs(lev+1, n/3)
        elif(n % 2 == 0):
            if(a[n//2] > lev + 1):
                a[n // 2] = lev + 1
                dfs(lev+1, n/2)
        else:
            dfs(lev+1, n-1)

if __name__ == "__main__":
    n = int(input())
    a = [0] * (MAX + 1)
    ret = 1
    cnt = 0
    dfs(0, n)
    print(a[1])
