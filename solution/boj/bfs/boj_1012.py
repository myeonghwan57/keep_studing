#유기농 배추 - 배추흰지렁이는 배추 근처에 서식하며 해충을 잡아먹는다.
#어떤 배추에 한마리의 배추흰지렁이가 살고 있으면 이 지렁이는 인접한 배추로 이동가능
#상하좌우 네 방향으로만 이동 가능
#1은 배추가 심어져 있는곳 0은 없는곳 
T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):
    queue = [(x,y)]
    field[x][y] = 0
    while queue:
        x,y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if field[nx][ny] == 1: 
                queue.append((nx,ny))
                field[nx][ny] = 0

for i in range(T):
    M, N, K = map(int,input().split())
    field = [[0]*(N) for _ in range(M)]
    cnt = 0

    for _ in range(K):
        x,y = map(int,input().split())
        field[x][y] = 1

    for i in range(M):
        for j in range(N):
            if field[i][j] == 1:
                BFS(i,j)
                cnt += 1
    print(cnt)        