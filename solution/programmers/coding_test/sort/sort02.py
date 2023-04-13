# 오답 - 시간 초과
# from itertools import permutations
# def solution(numbers):

#     num_list = list(permutations(numbers,len(numbers)))
#     int_list = []
#     for num in num_list:    
#         int_list.append(int(("").join(map(str,num))))
 
#     return str(max(int_list))

# print(solution([6,2,10]))

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))