dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == "__main__":
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    # m = int(input())
    # b = [list(map(int, input().split())) for _ in range(m)]
    a_n = len(a)
    # a = 0 과 b = 1이 맞아야됌, a의 1이 b= 1을 만나서는 안됌
    a_1 = []
    for i in range(a_n):
        for j in range(a_n):
            if(a[i][j] == 1):
                a_1.append((i, j))

    for v in a_1:
        x = v[0]
        y = v[1]
        print(x, y)
        print()
        for i in range(4):
            for j in range(a_n-1):
                xx = x + dx[i]
                yy = y + dy[i]
                if(0<=xx<n and 0<=yy<n):
                    print(xx, yy)
        print()
