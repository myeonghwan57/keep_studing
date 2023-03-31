# N개의 수중에서 어떤 다른 수 두개의 합으로 나타낼수 있으면 GOOD
N = int(input())
num_list = list(map(int,input().split()))
result = {}
for i in range(0,N-1):
    for j in range(i+1,N):
        if num_list[i] + num_list[j] in num_list:
            result[num_list[i]+num_list[j]] = 1

print(sum(result.values()))