if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(int(input()))
    a.sort()
    d = [9999999] * (m+1)
    d[a[0]] = 1
    d[a[1]] = 1
    for i in range(a[0], m+1):
        for j in a:
            if(i % j == 0):
                d[i] = min(d[i-j]+1, a[i-1])