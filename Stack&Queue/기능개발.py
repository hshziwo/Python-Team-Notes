def solution(progresses, speeds):
    answer = []
    
    while progresses :
        visited = []
        count = 0
        while progresses[0] < 100 :
            for i in range(len(progresses)) :
                progresses[i] += speeds[i]
                
        for j in range(len(progresses)) :
            if progresses[j] > 99 :
                count += 1
                visited.append(j)
            else :
                break
                
        progresses = [progresses[i] for i in range(len(progresses)) if i not in visited]
        speeds = [speeds[i] for i in range(len(speeds)) if i not in visited]

        if count > 0 :
            answer.append(count)
        
    return answer