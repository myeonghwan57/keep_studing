# 포켓몬 N 마리중 N/2마리 가져가도 된다 
# 종류에 따라 번호 붙임 
# ex 4마리 3,1,2,3 이면 

def solution(nums):

    answer = len(set(nums))
    if len(nums)/2> answer:
        return answer
    else:
        return len(nums) / 2
   
nums = list(map(int,input().split()))
print(solution(nums))