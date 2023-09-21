def solution(participant, completion):
    answer = ''

    hash_map = {}
    for i in participant :
        if i in hash_map :
            hash_map[i] += 1
        else :
            hash_map[i] = 1

    for i in completion :
        hash_map[i] -= 1

    sorted_hash_map = sorted(hash_map.items(), key = lambda x: x[1], reverse=True)
    answer = sorted_hash_map[0][0]
    return answer