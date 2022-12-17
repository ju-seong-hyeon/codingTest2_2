
if __name__ == "__main__":
    a = list(map(int, input()))
    a_sum = 0
    n = len(a)

    for i in range(0, n//2):
        a_sum += a[i]
    for j in range(n//2, n):
        a_sum -= a[j]

    if(a_sum == 0):
        print("LUCKY")
    else:
        print("READY")