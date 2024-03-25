from sys import stdin

n = int(stdin.readline().rstrip())

s = 0

for i in range(n):
    s += (i+1)

print(s)