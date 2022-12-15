if __name__ == "__main__":
    a = list(map(int, input().split()))
    n = len(a)
    k = int(input())
    cur = 0

    i = 0
    while(k>0):
        cur = i % n
        if(a[cur] > 0):
            a[cur] -= 1
            k -= 1
        i += 1
        # print(k)
    # print(a)
    for i in range(1, 1 + n):
        v = (cur + i) % n
        if(a[v] > 0):
            print(v+1)
            break
    else:
        print(-1)



