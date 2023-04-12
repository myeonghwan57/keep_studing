#암호 만들기 
#서로 다른 L 개의 알파벳 소문자들로 구성된 최소 한개의 모음(aeiou) 두개의 자음 구성 
#알파벳이 증가하는 순서 abc 
#사용한 가지수 C
from itertools import combinations
L,C = map(int,input().split())
alp_list = sorted(input().split())
word_list = list(combinations(alp_list,L))
vowels = ['a','e','i','o','u']
for word in word_list:
    vowel = 0
    consonant = 0
    for ch in word:
        if ch in vowels:
            vowel += 1
        else:
            consonant += 1
    if vowel >= 1 and consonant >=2:
        print("".join(word))

