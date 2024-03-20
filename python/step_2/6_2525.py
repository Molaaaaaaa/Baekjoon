from sys import stdin

a, b = map(int, stdin.readline().split())
c = int(stdin.readline().rstrip())

e = c % 60

b += c


while b >= 60:
    a += 1
    b -= 60

while a > 24:
    a -= 24

if a == 24:
    a = 0

print(a, b)