def solution(operations):
    answer = []
    for op in operations :
        a, b = op.split()
        
        if a == "I" :
            answer.append(int(b))
            answer.sort()
        elif a == "D" and len(answer) > 0:
            if b == "1" :
                answer.pop()
            elif b == "-1" :
                answer.pop(0)
                
    if len(answer) > 0 :
        return [answer[-1],answer[0]]
    else :
        return [0,0]