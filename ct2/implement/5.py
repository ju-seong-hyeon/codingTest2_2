from collections import deque

dx_r = [0, 1]
dx_l = [0, -1]
dx_u = [-1, 0]
dx_d = [1, 0]

if __name__ == "__main__":
    n = int(input()) # 맵 크기
    k = int(input()) # 사과 개수
    a = [[0] * n for _ in range(n)]
    dq = deque()

    for _ in range(k):
        k_x, k_y = map(int, input().split())
        a[k_x][k_y] = 1

    v = int(input())
    for _ in range(v):
        v_n, v_d = input().split()
        v_n = int(v_n)
        dq.append((v_n, v_d))

    cur_x, cur_y = (0, 0)
    cnt = 0
    a[cur_x][cur_y] = 2

    cur = dq.popleft()
    v_n, v_d = cur[0], cur[1]
    if (v_d == 'D'):
        xx, yy = dx_d
    elif (v_d == "L"):
        xx, yy = dx_l
    elif (v_d == 'R'):
        xx, yy = dx_r
    else:
        xx, yy = dx_u

    while(1):
        for _ in range(v_n):
            cnt += 1
            if (cnt == v_d):
                cur = dq.popleft()
                v_n, v_d = cur[0], cur[1]
                if (v_d == 'D'):
                    xx, yy = dx_d
                elif (v_d == "L"):
                    xx, yy = dx_l
                elif (v_d == 'R'):
                    xx, yy = dx_r
                else:
                    xx, yy = dx_u

            cur_xx = cur_x + xx
            cur_yy = cur_y + yy

            if(0<=cur_xx<n and 0<=cur_yy<n):
                if(a[cur_xx][cur_yy] == 1):
                    a[cur_xx][cur_yy] = 2
                elif(a[cur_xx][cur_yy] == 2):
                    break
                else:
                    a[cur_x][cur_y] = 0
            else:
                break
    print(cnt)