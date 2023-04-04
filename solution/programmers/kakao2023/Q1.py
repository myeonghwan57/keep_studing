#고객의 약관 동의 1~n 번으로 분류되는 개인정보 n 유효기간 있음 
# A-6 / B-12/ c-3 
#today 문자열 유효기간 terms 배열 privacies 문자열 
def dateToDay(date):
    year, month, day = map(int, date.split("."))
    return (year * 12 * 28) + (month * 28) + day
def solution(today, terms, privacies):
    answer = []

    today = dateToDay(today)

    termsInfo = dict()
    for term in terms:
        term = term.split()
        termsInfo[term[0]] = int(term[1]) * 28
    
    for i in range(len(privacies)):
        date, term = privacies[i].split()
        if dateToDay(date) + termsInfo[term] <= today:
            answer.append(i+1)
        
    return answer
