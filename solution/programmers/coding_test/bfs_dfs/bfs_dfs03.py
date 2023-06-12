from collections import deque
def solution(maps):
    answer = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    #방문
    visited = [[False]*len(maps[0]) for _ in range(len(map))]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        #내가 있는 위치
        visited[0][0] = True
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 < nx < len(maps) and 0 < ny < len(maps[0]) and maps[nx][ny] == 1: 
                    if visited[nx][nx] == 'False':
                        visited[nx][ny] == True
                        maps[nx][ny] = maps[x][y] + 1
                        queue.append((nx, ny))      
        
        return maps[len(maps)-1][len(maps[0])-1]
    
    answer = bfs(0, 0)
    
    return -1 if answer == 1 else answer   