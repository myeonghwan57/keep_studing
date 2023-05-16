import math
def solution(r1, r2):
    answer = 0
    cnt = 0
    for i in range(r2+1):
        for j in range(r2+1):
            if math.pow(i,2)+math.pow(j,2) >= math.pow(r1,2) and math.pow(i,2)+math.pow(j,2) <= math.pow(r2,2):
                answer += 1
                if i == 0 or j == 0:
                    cnt += 1
    return (answer-cnt) * 4 + 2*cnt

print(solution(2,3))