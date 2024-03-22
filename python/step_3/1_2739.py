from sys import stdin

N = int(stdin.readline().rstrip())

for i in range(9):
    print(f"{N} * {i + 1} = {N * (i + 1)}")