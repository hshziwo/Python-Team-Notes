def solution(n, costs):
    answer = 0
    sorted_costs = sorted(costs, key= lambda x : x[2])
    visited = [False for _ in range(n)]
    for x in sorted_costs :
        visited[x[0]] = True
        visited[x[1]] = True
        answer += x[2]
        check = True
        for y in visited : 
            if y == False :
                check = False
                break
        if check == True :
            break
    
    return answer


def solution(n, costs):
    answer = 0
    sorted_costs = sorted(costs, key= lambda x : x[2])
    visited = [False for _ in range(n)]
    union = set([])
    for x in sorted_costs :
        if x[0] in union and x[1] in union :
            continue
        union.add(x[0])
        union.add(x[1])
        visited[x[0]] = True
        visited[x[1]] = True
        answer += x[2]
        check = True
        for y in visited : 
            if y == False :
                check = False
                break
        if check == True :
            break
    
    return answer