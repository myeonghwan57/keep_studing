# 백준 1316번 그룹단어 체크 
# 그룹단어랑 단어에 존재하는 모든 문자가 연속해서 나오는경우 
N = int(input())
cnt = N
for i in range(N):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break
print(cnt)

