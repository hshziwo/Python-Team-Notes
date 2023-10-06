def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations),0,-1) :
        h = 0
        for j in citations :
            if j >= i :
                h += 1
            else :
                break
        
        if h >= i:
            answer = i
            break
    return answer