# 추월 2002
#N개의 차량이 지나가고 자신이 가지고 있는 목록에서 어떤 차량이 추월했는지 

N = int(input())
cnt = 0
car_in, car_out = dict(), []
for i in range(N):
	car = input()
	car_in[car] = i
for _ in range(N):
	car = input()
	car_out.append(car)
 
for i in range(N-1):
	for j in range(i+1, N):
		if car_in[car_out[i]] > car_in[car_out[j]]:
			cnt += 1
			break
print(cnt)