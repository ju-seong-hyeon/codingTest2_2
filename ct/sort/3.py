n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse= True)
for i in range(m):
    if(a[i] < b[i]):
        a[i] = b[i]
    else:
        break3
print(sum(a))