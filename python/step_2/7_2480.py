from sys import stdin

a, b, c = map(int, stdin.readline().split())

ls = [a, b, c]
ls_2 = []

for i in ls:
    if i in ls_2:
        num = i
        continue
    ls_2.append(i)

ls_sort = list(set(ls))
n = len(ls_sort)

if n == 1:
    print(10000 + (a * 1000))
elif n == 2:
    print(1000 + (num * 100))
else:
    print(max(ls) * 100)