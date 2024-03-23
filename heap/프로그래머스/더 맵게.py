import heapq
def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    if scoville[0] >= K :
        return answer
    
    scoville_score = 0
    while scoville_score < K :
        try :
            result1 = heapq.heappop(scoville)
            result2 = heapq.heappop(scoville)
        except :
            return -1
            
        tmp = result1 + result2 * 2
        
        if len(scoville) > 0 :
            scoville_score = min(scoville[0],tmp)
        else :
            scoville_score = tmp
            
        heapq.heappush(scoville, tmp)
        answer += 1
        
    return answer