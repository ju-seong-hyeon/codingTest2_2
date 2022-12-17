

if __name__ == "__main__":
    a = list(map(str, input()))
    b = []
    a_sum = 0

    for i in a:
        if('A' <= i <= 'Z'):
            b.append(i)
        else:
            i = int(i)
            a_sum += i

    b.sort()

    for i in b:
        print(i, end = "")

    print(a_sum)