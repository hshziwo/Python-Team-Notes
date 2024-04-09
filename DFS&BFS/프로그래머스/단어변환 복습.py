# 못 풀어서 정답 보고 다시 복습함.
# BFS 문제
from collections import deque


# 현재 단어와 비슷한 단어들 리턴
def get_adjacent_words(current, words):
    for word in words:
        count = 0
        for c, w in zip(current, word):
            # 한 글자씩 비교해서 한 글자 다를 때마다 +1
            if c != w:
                count += 1

        # 딱 한글자만 차이가 난다면 yield로 generator에 추가
        if count == 1:
            yield word


def solution(begin, target, words):
    # 먼저 현재 시작단어 방문값을 0으로 초기화
    visited = {begin: 0}
    # 큐에 시작 단어 넣음
    queue = deque([begin])
    while queue:
        current = queue.popleft()

        # queue를 이용한 BFS 문제
        # yield를 이용한 generator값 이용
        for next_word in get_adjacent_words(current, words):
            # 다음 단어가 visited에 없으면 현재 방문count에 +1을 해서
            # visited에 추가하고 queue에 append한다.
            if next_word not in visited:
                visited[next_word] = visited[current] + 1
                queue.append(next_word)
            # 이미 visited한 단어는 그냥 넘어간다.
            # BFS가 모두 끝나면 최소 방문수가 visited에 업데이트 되어 있다.

    # target에 대한 방문값을 get하고 없을 시 0을 리턴한다.(== dict.get(target, 0))
    return visited.get(target, 0)
