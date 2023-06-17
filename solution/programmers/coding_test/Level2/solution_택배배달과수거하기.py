def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0

    delivery = 0
    pick = 0

    for i in range(n):
        delivery += deliveries[i]
        pick += pickups[i]

        while delivery > 0 or pick > 0:
            delivery -= cap
            pick -= cap
            answer += (n - i) * 2

    return answer