import itertools
def solution(k, dungeons):
    count_array = []
    permu = itertools.permutations(range(len(dungeons)), len(dungeons))
    for x in list(permu) :
        tmp = k
        count = 0
        for i in x :
            min_value , value = dungeons[i]
            if tmp >= min_value :
                tmp -= value
                count += 1
        count_array.append(count)
        
    return max(count_array)