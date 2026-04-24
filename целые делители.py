import math
x = int(input())
con = 0
y = int(math.isqrt(x))
for i in range(1, y + 1):
    if x % i == 0:
        if i * i == x:
            con += 1
        else:
            con += 2
print(con)