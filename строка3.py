m = int(input())
n = int(input())
mass = [int(input()) for i in range(n)]
mass.sort()
l = 0
r = n -1
b = 0
while l <= r:
    if mass[l] + mass[r] <= m:
        l += 1
    r -= 1
    b += 1
print(b)