def solution(players, callings):
    # 바뀌는 것을 value로 둠 (순위)
    rank = dict()
    for i in range(len(players)):
        rank[players[i]] = i
    
    for player in callings:
        nowIndex = rank.get(player)    
        players[nowIndex], players[nowIndex - 1] = players[nowIndex - 1], players[nowIndex]
        rank[players[nowIndex]] = nowIndex
        rank[players[nowIndex - 1]] = nowIndex - 1
    
    return players