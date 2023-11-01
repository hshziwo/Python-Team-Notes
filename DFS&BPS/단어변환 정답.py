from collections import deque
def solution(begin, target, words):    
    def get_adjacent(word) :
        array = []
        for tmp in words :
            count = 0
            if word == tmp :
                continue
            for i in range(len(word)) :
                if word[i] == tmp[i] :
                    count += 1
            if count == len(word) - 1 :
                array.append(tmp)
        return array
    
    # bfs 방식
    visited = {begin : 0}
    queue = deque([begin])
    
    while queue :
        word = queue.popleft()
        cands = get_adjacent(word)
        for cand in cands :
            if cand not in visited :
                visited[cand] = visited[word] + 1
                queue.append(cand)
    
    # key가 없으면 0을 주기 위함
    return visited.get(target,0)

# 아래는 더 효율적인 방식
from collections import deque


def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)