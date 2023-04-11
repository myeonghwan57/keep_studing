def solution(brown, yellow):
    answer = []
    num_list = []
    for i in range(1,(brown+yellow)//2):
        m = [0,0]
        if (brown+yellow) % i == 0:
            m[0] = i
            m[1] = (brown+yellow) // i
        num_list.append(m)
    
    for num in num_list:
        if (num[0]*2) + (num[1]*2) - 4 == brown:
            answer.append(num)
    return max(answer)
print(solution(10,2))