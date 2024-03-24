# 아파트 갯수, 기지국이 설치된 배열, 기지국의 전파거리가 주어질 때 최소 몇개의 기지국을 더 설치해야 전파가 닿는지
# https://school.programmers.co.kr/learn/courses/30/lessons/12979
# 해설
# https://hoons-dev.tistory.com/68

import math


def solution(n, stations, w):
    answer = 0
    rest = []

    before_end = 0
    for s in stations:
        start, end = max(s - w, 1), min(s + w, n)
        if not before_end:
            rest.append(start - 1)
            before_end = end
        else:
            if before_end + 1 < start:
                # 안 겹치는 경우
                rest.append(start - before_end - 1)
            before_end = end

    rest.append(n - before_end)

    for r in rest:
        cover = 1 + 2 * w
        answer += math.ceil(r / cover)

    return answer
