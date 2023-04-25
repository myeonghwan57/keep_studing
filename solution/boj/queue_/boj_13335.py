#다리 위에는 w대의 트럭만 동시에 올라갈수 있다.
N, W, L = map(int,input().split())
truck = list(map(int,input().split()))

bridge = [0] * W
time = 0
while bridge:
    time += 1
    bridge.pop(0)
    if truck:
        if sum(bridge) + truck[0] <= L:
            bridge.append(truck.pop(0))
        else: 
            bridge.append(0)
print(time)


