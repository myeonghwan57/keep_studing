#n명의 사용자 M개 판매 
# 할인율은 10 20 30 40 이모티콘 마다 할인율 다름.
# 이모티콘 모두 구매, 자신이 정한 일정 할인율 이상이 되면 모두 구매 
# 자신이 생각하는 가격 이상이 되면 구독함

def solution(users, emoticons):
    answer = [0,0]
    for user in users:
        ratio, price = user.split()
        all_price = 0
        for emoticon in emoticons :
            emo_ratio, emo_price = emoticon.split()
            if emo_ratio >= ratio:
                all_price += emo_price*(100-emo_ratio) // 100
        if price > all_price:
            answer[1]+=all_price
        else:
            answer[0] += 1
    
    return answer
