
if __name__ == "__main__":
    a = input()
    n = len(a)
    a_min = n
    v = 1

    # while(v < n//2):
    #     a_cur = ""
    #     cnt = 1
    #     cur = a[0 : v]
    #     for i in range(v, n+1-v):
    #         if(cur == a[i : i+v]):
    #             cnt += 1
    #             if(i == n-v):
    #                 a_cur += str(cnt)
    #                 a_cur += cur
    #         else:
    #             if (cnt != 1):
    #                 a_cur += str(cnt)
    #                 cnt = 1
    #             a_cur += cur
    #             cur = a[i : i+v]
    #
    #     v += 1
    #     print(a_cur, len(a_cur))
    #     a_min = min(len(a_cur), a_min)

    v = 2
    cnt = 1
    cur = a[0: v]
    # print(cur)
    a_cur = ""
    for i in range(v, n):
        print(cur)
        if(cur == a[i:i+v]):
            cnt += 1

            if(i== n+1-v):
                a_cur += str(cnt)
                a_cur += cur
        else:
            if(cnt != 1):
                a_cur += str(cnt)
                cnt = 1
            a_cur += cur
            cur = a[i : i + v]


    print(a_cur)
    print(a_min)