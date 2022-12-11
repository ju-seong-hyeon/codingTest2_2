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
    cnt = k * m//(k + 1)
    cnt += m % (k + 1)
    # print(cnt)
    a_sum += cnt * a[0]
    a_sum += (m - cnt) * a[1]
    print(a_sum)