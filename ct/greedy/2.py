
if __name__ == "__main__":
    n,m,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse = True)
    # cnt = m//k
    # cnt_v = k-(cnt*k)
    # print(cnt, cnt_v)
    # a_sum = cnt * k * a[0] + cnt_v * cnt[1]
    # print(a_sum)
    a_sum = 0
    cnt = 0
    while(m>0):
        if(cnt < k):
            a_sum += a[0]
            cnt+=1
            m-=1
        else:
            a_sum += a[1]
            cnt = 0
            m-=1
    print(a_sum)

    # while (m > 0):
    #     if (m // k > 1 and cnt == 0):
    #         a_sum += (k * a[0])
    #         cnt += k
    #         m -= k
    #     elif(m//k>1 and cnt != 0):
    #         a_sum += a[1]
    #         cnt = 0
    #         m -= 1
    #     elif(m//k == 0):
    #         a_sum += (m * a[0])
    #         m = 0
    #     print(a_sum)
    # print(a_sum)
