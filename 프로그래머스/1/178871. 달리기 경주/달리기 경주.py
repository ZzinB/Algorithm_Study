def solution(players, callings):
    player_rank = {player : rank for rank, player in enumerate(players)}
    rank_player = {rank : player for rank, player in enumerate(players)}
    
    for calling in callings:
        calling_player_rank = player_rank[calling] 
        front_player_rank = calling_player_rank-1 
        front_player = rank_player[front_player_rank]  
        
        rank_player[calling_player_rank] = front_player 
        rank_player[front_player_rank] = calling
        
        player_rank[calling] = front_player_rank
        player_rank[front_player] = calling_player_rank
        
    
    return list(rank_player.values())
