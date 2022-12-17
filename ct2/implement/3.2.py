a = input()
for i in range(1, len(a) // 2 +1):
    v = ""
    cur = a[0:i]
    cnt = 1

    for j in range(i, len(a), i):
        if cur == a[j:j+i]:
            cnt += 1
        else:
            v = str(cnt) + cur