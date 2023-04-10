#n명의 사용자 M개 판매 
# 할인율은 10 20 30 40 이모티콘 마다 할인율 다름. 각각의 할인율로 정해짐 
# 이모티콘 모두 구매, 자신이 정한 일정 할인율 이상이 되면 모두 구매 
# 자신이 생각하는 가격 이상이 되면 구독함
from itertools import product
def solution(users, emoticons):
    subscriber_cnt = 0
    max_price = 0
    dataset = product([10,20,30,40],repeat=len(emoticons))
    for data in dataset:
        user_cnt = 0
        sum_price = 0
        for user in users:
            total = 0
            for i in range(len(emoticons)):
                if data[i] >= user[0]:
                    total += (100-data[i])*emoticons[i]/100
            if total >= user[1]:
                user_cnt += 1
            else:
                sum_price += total
        
        if subscriber_cnt < user_cnt:
            subscriber_cnt = user_cnt
            max_price = sum_price
        elif subscriber_cnt == user_cnt:
            if max_price < sum_price:
                max_price = sum_price
    return [subscriber_cnt,max_price]
        


    
print(solution([[40,10000],[25,10000]],[7000,9000]))

# dataset =  [10,20,30,40]
# saledata = list(product(dataset,repeat = 2))

# print(saledata[1][1])