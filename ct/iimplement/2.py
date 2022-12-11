

if __name__ == "__main__":
    n = int(input())
    v = ""
    cnt = 0
    for i in range(n+1):
        for j in range(0, 60):
            for k in range(0, 60):
                time = str(i)
                min = str(j)
                sec = str(k)
                v = time + min + sec
                if '3' in v:
                    cnt += 1
    print(cnt )
