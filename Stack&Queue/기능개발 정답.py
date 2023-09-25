def solution(progresses, speeds):
    answer = []
    
    while progresses :
        count = 0
        while progresses[0] < 100 :
            for i in range(len(progresses)) :
                progresses[i] += speeds[i]

        while progresses and progresses[0] >= 100 :
            del progresses[0], speeds[0]
            count += 1

        if count > 0 :
            answer.append(count)
        
    return answer