# https://school.programmers.co.kr/questions/49151
# ㄱ) 조건 만족하는 최대값 구할 때 참고
# https://school.programmers.co.kr/questions/41679
# https://school.programmers.co.kr/questions/31861 이건 그냥 참고


def solution(distance, rocks, n):
    rocks.sort()
    d = [rocks[0]]
    for i in range(1, len(rocks)) :
        d.append(rocks[i] - rocks[i-1])
    d.append(distance - rocks[len(rocks) - 1])

    start, end = 0, distance
    while start < end :
        mid = (start + end + 1) // 2
        removedStone = 0
        cur = 0
        for i in range(len(d)) :
            cur += d[i]
            if cur < mid :
                # 현재보다 작으면 추가
                removedStone += 1
            else :
                cur = 0

        if removedStone <= n:
            start = mid
        else :
            end = mid - 1

    answer = start
    return answer