 #소수 찾기 
from itertools import permutations
def is_prime_number(x) :
    if x < 2 :
        return False
    
    for i in range(2, x) :
        if x % i == 0 :
            return False
            
    return True
def solution(numbers):
    answer = 0
    num_list = []
    for i in range(1,len(numbers)+1):
        num_list += list(permutations(numbers,i))
    int_list = []
    for num in num_list:
        result = int(("").join(map(str,num)))
        int_list.append(result)
    result_list = list(set(int_list))
    for n in result_list:
        if is_prime_number(n) == True:
            answer += 1
    return answer
 
print(solution([0,1,1]))