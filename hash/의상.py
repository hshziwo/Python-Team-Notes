def solution(clothes):
    hash_map = {}
    for i in clothes :
        if i[1] in hash_map :
            hash_map[i[1]].append(i[0])
        else :
            hash_map[i[1]] = [i[0]]
    
    answer = 1
    for i in hash_map.values() :
        tmp = len(i) + 1
        answer *= tmp
            
    answer -= 1

    return answer