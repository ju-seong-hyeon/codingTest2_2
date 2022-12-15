if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = set()
    cnt = 0

    for i in range(n-1):
        for j in range(i+1, n):
            if(a[i] != a[j]):
                cnt += 1
    print(cnt)