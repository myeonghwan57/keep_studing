import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    call = [str(sys.stdin.readline().strip()) for _ in range(n)] 
    call.sort() 
    chek = "yes" 
    
    for i in range(len(call) - 1):

        if call[i] == call[i + 1][0:len(call[i])]:
            chek = "no"

    if chek == "no":
        print("NO")
    else:
        print("YES")