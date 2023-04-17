#최소 필요 피로도 // 탐험을 위해 가지고 있어야 하는 최소한의 피로도 
# 소모 피로도 // 참헌한후 소모되는 피로도 
from itertools import permutations
def solution(k, dungeons):
    answer = []
    case_list = list(permutations([x for x in range(len(dungeons))], len(dungeons)))
    
    for case_ in case_list:
        now = k
        cnt = 0
        for i in case_:
            if now >= dungeons[i][0]:
                now -= dungeons[i][1]
                cnt += 1
        answer.append(cnt)

    return max(answer)
print(solution(80,[[80,20],[50,40],[30,10]]))