def solution(array, commands):
    answer = []
    
    for command in commands :
        i = command[0]
        j = command[1]
        k = command[2]
        
        tmp_array = array[i-1:j]
        tmp_array.sort()
        return_value = tmp_array[k-1]
        answer.append(return_value)
    return answer