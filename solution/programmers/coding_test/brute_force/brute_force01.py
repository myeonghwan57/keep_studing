#명함지갑을 만드는 회사 지갑 크기 정하기.
# 1	60	50
# 2	30	70
# 3	60	30
# 4	80	40
def solution(sizes):
    w = []
    h = []

    for i in range(len(sizes)):
        w.append(max(sizes[i]))
        h.append(min(sizes[i]))

    return max(w)*max(h)


print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))