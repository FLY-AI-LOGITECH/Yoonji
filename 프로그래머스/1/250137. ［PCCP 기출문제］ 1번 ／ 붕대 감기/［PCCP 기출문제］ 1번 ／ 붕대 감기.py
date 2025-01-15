def solution(bandage, health, attacks):
    
    accumulation = 0 #연속 성공 횟수 
    i = 0
    time = 0
    max_health = health
    
    while i < len(attacks):
        if i < len(attacks) and time == attacks[i][0]:
            
            health = health - attacks[i][1]
            if health <= 0:
                return -1 
            
            i = i +1
            accumulation = 0
        else: 
            health = health + bandage[1]
            if health > max_health:
                health = max_health
                
            accumulation = accumulation + 1
            
            if accumulation == bandage[0]:
                health = health + bandage[2]
                if health > max_health:
                    health = max_health
                accumulation = 0
                
        time += 1
    return health