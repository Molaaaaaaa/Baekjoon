from sys import stdin

a = int(stdin.readline().rstrip())
b = stdin.readline().rstrip()

ls = []
total = 0
seq = 0

for i in range(len(b)):

    
    ls.append(b[i])


for i in ls[::-1]:
    tmp = a * int(i)
    print(tmp)
    total +=  int(str(tmp) + ("0" * seq))
    seq += 1

print(total)

