N = int(input())

stack = []
calc = []
cnt = 1
tmp = True
for i in range(N):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        calc.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        calc.append('-')
    else:
        tmp = False
if tmp == False:
    print('NO')
else:
    for i in calc:
        print(i)    
