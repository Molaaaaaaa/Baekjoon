from sys import stdin

h, m = map(int, stdin.readline().split())

if m < 45:
    m += 15
    if h == 0:
        h = 23
    else:
        h -= 1
else:
    m -= 45    

print(h, m)

# 고려할 사항
# 0시 자정, 45분 이전, 이후의 시각