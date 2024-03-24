from sys import stdin

T = int(stdin.readline().rstrip())

for i in range(T):
    A, B = map(int, stdin.readline().split())
    print(A + B)
