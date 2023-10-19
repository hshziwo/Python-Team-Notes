def solution(people, limit):
    people.sort(reverse=True)
    count = 0
    while people :
        weight = people.pop(0)
        for i in range(len(people)) :
            if limit >= weight + people[i] :
                weight += people[i]
                del people[i]
                break
        count += 1
    return count


def solution(people, limit):
    people.sort(reverse=True)
    count = 0
    visited = [False for _ in range(len(people))]
    for i in range(len(people)) :
        if visited[i] == True :
            continue
        visited[i] = True
        weight = people[i]
        for j in range(i+1, len(people)) :
            if visited[j] == False and limit >= weight + people[j] :
                weight += people[j]
                visited[j] = True
                break
        count += 1
    return count


def solution(people, limit):
    answer = 0
    people.sort()
    visited = [False for _ in range(len(people))]
    for i in range(len(people)) :
        if visited[i] == True :
            continue
        first = people[i]
        second_max = 0
        second_idx = i
        for j in range(i+1, len(people)) :
            if visited[j] == True :
                continue
            second = people[j]
            if first + second > limit :
                break
            else :
                second_max = second
                second_idx = j
        visited[i] = True
        visited[second_idx] = True
        answer += 1
    
    return answer