#사과를 먹으면 뱀의 길이가 늘어난다.
#처음 뱀의 길이는 1 맨위 맨 좌측에 위치/ 처음 진행방향은 오른쪽/ 상하좌우에 벽 존재
# 벽이나 자기 몸에 닿으면 게임 종료

N = int(input())
K = int(input())
#게임맵, 0으로 표시 
data = [[0]*(N+1)for _ in range(N+1)]

move_info = []
#사과가 있는곳은 1로 표시.
for _ in range(K):
    a,b = map(int,input().split())
    data[a][b] = 1
#움직임 정보
L = int(input())
for _ in range(L):
    x, c = input().split()
    move_info.append(int(x),c)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4
    return direction