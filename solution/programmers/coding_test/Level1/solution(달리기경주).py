def solution(players, callings):
    temp = ''
    for i in range(len(callings)):
        for j in range(len(players)):
            if  callings[i] == players[j]:
                temp = players[j]
                players[j] = players[j-1]
                players[j-1] = temp   
                
    return players

players = ["mumu", "soe", "poe", "kai", "mine"]	
callings = ["kai", "kai", "mine", "mine"]

print(solution(players,callings))