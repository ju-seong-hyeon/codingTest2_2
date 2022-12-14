

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    ll = 0
    lr = a[-1]
    a_max = 0

    while(ll<=lr):
        mid = (ll + lr) // 2
        a_sum = 0

        for i in a:
            if(i > mid):
                a_sum += (i - mid)

        # if(a_sum == m):
        #     lr = mid - 1
        #     a_max = max(a_max, mid)
        # elif(a_sum < m):
        #     ll = mid + 1
        # else:
        #     lr = mid - 1

        if(a_sum == m):
            ll = mid + 1
            a_max = max(a_max, mid)

        elif(a_sum < m):
            lr = mid - 1
        else:
            ll = mid + 1

        print(a_sum, mid, a_max)

    print(a_max)