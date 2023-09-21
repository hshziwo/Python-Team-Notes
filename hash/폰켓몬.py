def solution(nums):
    answer = 0
    hash_map = {}
    for i in nums :
        hash_map[i] += 1
    
    count = 0
    visited = []
    keys = list(hash_map.keys())
    while count < len(nums) / 2 :
        for i in keys :
            if i not in visited :
                answer += 1
                visited.append(i)
                
            if hash_map[i] > 0 :
                hash_map -= 1
                count += 1
                
            if count == len(nums) / 2 :
                break
                
    return answer

solution([3,1,2,3])