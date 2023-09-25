def solution(arr):
    answer = []
    for i in arr :
        if len(answer) == 0 or answer[len(answer) - 1] != i :
            answer.append(i)
    
    return answer