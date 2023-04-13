def solution(array, commands):
    answer = []
    for command in commands:
        num_list = []
        for i in range(command[0]-1, command[1]):
            num_list.append(array[i])
        num_list.sort()
        answer.append(num_list[command[2]-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))