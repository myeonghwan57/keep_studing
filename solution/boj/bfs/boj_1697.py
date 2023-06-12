#숨바꼭질
#수빈이는 점N 동생은 점K 에 있다. 수빈이는 걷거나 순간이동 가능.
#수빈이는 x일때 x-1 이나 x+1로 이동가능 순간이동을 하게 되면 2x로 이동 
# 수빈이와 동생의 위치가 주어졌을때 수빈이가 동생을 찾을수 있는 가장 빠른시간을 구하시오.

import sys
from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return visited[v]
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)

n, k = map(int, sys.stdin.readline().split())
visited = [0 for i in range(100001)]
print(bfs(n))