def solution(s):
    answer = False
    
    count = 0
    for i in s :
        if count > -1 :
            if i == "(" :
                count += 1
            elif i == ")" :
                count -= 1
                
    if count == 0 :
        answer = True

    return answer