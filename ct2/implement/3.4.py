

if __name__ == "__main__":
    a = input()
    n = len(a)
    a_min = n
    v = 1
    while(v < n//2+1):
        a_cur = ""
        cur = a[:v]
        cnt = 1

        for i in range(v, n+v, v):
            if(cur == a[i : i + v]):
                cnt += 1
            else:
                if(cnt == 1):
                    a_cur += cur
                else:
                    a_cur += str(cnt)
                    a_cur += cur
                    cnt = 1
                cur = a[i : i + v]

        v += 1
        a_min = min(len(a_cur), a_min)
    print(a_min)

