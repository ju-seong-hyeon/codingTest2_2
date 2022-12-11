n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
a_min = 0
for i in range(len(a)):
    v = min(a[i])
    a_min = max(a_min, v)
print(a_min)