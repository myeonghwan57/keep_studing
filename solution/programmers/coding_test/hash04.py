#2차원 배열 clothes 다른 옷의 조합수 return 
#의상의 이름 의상의 종류 
def solution(clothes):
    answer = 1
    dic = {}
    for i in range(len(clothes)):
        if clothes[i][1] in dic.keys():
            dic[clothes[i][1]].append(clothes[i][0])
        else: 
            dic[clothes[i][1]] = [clothes[i][0]]
    for value in dic.values():
        answer*=len(value) + 1

    return answer-1



clothes = [list(input().split()) for _ in range(3)]
print(solution(clothes))
