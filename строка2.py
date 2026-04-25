n = int(input())
num = list(map(int, input().split()))
num[:] = [num[-1]] + num[:-1]
print(' '.join(map(str, num)))