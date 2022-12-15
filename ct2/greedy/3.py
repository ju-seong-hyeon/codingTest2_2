
if __name__ == "__main__":
    a = list(map(int, input()))
    n = len(a)
    cnt1 = 0
    cnt2 = 0
    # 목표 0'
    obj = 0
    for i in range(1, n):
        if(a[i] != obj and a[i] != a[i-1]):
            cnt1 += 1
        elif(a[i] == obj and a[i] != a[i-1]):
            cnt2 += 1

    print(min(cnt1, cnt2))



    # 목표 1