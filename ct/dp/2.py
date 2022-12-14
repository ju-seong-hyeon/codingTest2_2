if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n+1)
    a_sum1 = 0
    a_sum2 = 0
    for i in range(0, n-1, 2):
        a_sum1 += a[i]
        a_sum2 += a[i + 1]

    print(max(a_sum1, a_sum2))