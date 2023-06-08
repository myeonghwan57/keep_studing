#N개의 센서 K개의 집중국 세울수 있다.
import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
sensor_list =list(map(int,input().split()))
if K >= N:
    print(0)
    sys.exit()
distance_list = []
sensor_list.sort()
for i in range(N-1):
    distance_list.append(sensor_list[i+1]-sensor_list[i])
distance_list.sort()
for _ in range(K-1):
    distance_list.pop()

print(sum(distance_list))