

if __name__ == "__main__":
    a = input()
    n = len(a)
    a_min = n
    a_cut = 1
    cur = ""
    cnt = 1
    for i in range(0, n):
        if(i<n-1):
            if(a[i] == a[i+1]):
                cnt += 1
            else:
                if(cnt != 1):
                    cur += str(cnt)
                    cnt = 1
                cur += a[i]
        else:
            if(a[i] == a[n-1]):
                cur += str(cnt)
                cur += a[i]

        a_min = min(a_min, len(cur))


    print(cur)
