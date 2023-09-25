def solution(priorities, location):
    answer = 0
    sorted_prior = sorted(priorities, reverse=True)
    
    queue = [(i,priorities[i]) for i in range(len(priorities))]
    
    while queue :
        if queue[0][1] == sorted_prior[0] :
            answer += 1
            
            if queue[0][0] == location :
                break
            
            del queue[0], sorted_prior[0]
        else :
            queue.append(queue[0])
            del queue[0]
            
    return answer