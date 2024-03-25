from sys import stdin
input = stdin.readline

x = int(input().rstrip())
n = int(input().rstrip())

sum = 0

for i in range(n):
    a, b = map(int, input().split())
    sum += (a * b)

if x == sum:
    print("Yes")
else:
    print("No")