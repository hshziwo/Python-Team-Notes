def solution(priorities, location):
    answer = 0
    sorted_prior = sorted(priorities, reverse=True)
    
    queue = [(i,priorities[i]) for i in range(len(priorities))]
    
    while queue :
        cur = queue.pop(0)

        if cur[1] == sorted_prior[0] :
            answer += 1
            sorted_prior.pop(0)

            if cur[0] == location :
                break
        else :
            queue.append(cur)
            
    return answer