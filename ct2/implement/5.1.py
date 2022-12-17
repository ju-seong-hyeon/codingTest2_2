from collections import deque
dx_d = [1, 0]
dx_l =

def ch_loc(cur_d, dir):
    x, y = cur_d[0], cur_d[1]
    if(dir == 'D'):
        x += 1
    else:
        y +=

if __name__ == "__main__":
    n = int(input())
    a = [[0] * n for _ in range(n)]
    k = int(input())
    cur_l = (0, 0, (0, 1))
    for _ in range(k):
        x, y = map(int, input().split())
        a[x][y] = 1
    v = int(input())
    dq = deque()
    for i in range(v):
        dx_n, dx_m = map(int, input().split())
        dx_n = int(dx_n)
        dq.append((dx_n, dx_m))

    for i in range(1, 10001):
        cur = dq.popleft()
        dx_n, dx_d = cur[0], cur[1]
        dx, dy = ch_loc(cur_l[2], dx_d)