import sys

a, b = map(int, sys.stdin.readline().split())
count = 1

while (a < b):
    if (b % 2 == 0):
        b = b // 2
    else:
        if (int(str(b)[-1]) == 1):
            b = int(str(b)[:-1])
        else:
            break
    count += 1

if (a == b):
    print(count)
else:
    print(-1)