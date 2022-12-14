n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

# a : 기준
# b : 찾을 것
a.sort()
b.sort()

for i in b:
    if i in a:
        print("yes", end = " ")
    else:
        print("no", end = " ")