a = "ababcdcd"
n = len(a)
v = 2
cur = a[: v]
cnt = 1
a_cur = ""
for i in range(v, n+v, v):
    if(cur == a[i : i+ v]):
        cnt += 1
        # if (i == n-v):
        #     a_cur += str(cnt)
        #     a_cur += cur

    else:
        if(cnt == 1):
            a_cur += cur
        else:
            a_cur += str(cnt)
            a_cur += cur

        cnt = 1
        cur = a[i : i + v]
        # print(a_cur)


print(a)
print(a_cur, len(a_cur))