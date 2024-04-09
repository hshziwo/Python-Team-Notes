# https://oh2279.tistory.com/231
# 블로그 참고해서 방법 공부하기
# 꽤 어려운 이분 탐색 문제이다,,

# 우선 첫번째 의문!

# 이게 왜 이분탐색이지? -> 사실 이것만 해결되면 금방 풀린다.

# 문제의 조건을 보면 범위가 10억(?맞나 암튼)이므로 완전탐색으론 풀 수 없다.

# 보통 조건의 범위가 어마무시하면 이분탐색인 경우가 많다! 이건 소소한 꿀팁

# 여기서 중요한 것은 '도대체 뭘 탐색할 것인가?' 이다.

# 이 문제에서는 돌을 n개 제거했을 때의 최소 거리들 중 최대 거리를 구해야 하므로, 우선 최소 거리를 이분 탐색으로 구해보자

# 1. 양 끝 점 (left, right)를 설정한다.

# 2. mid (left + right // 2) 를 설정한다.

# 3. 현재 위치와 다음 돌 사이의 거리를 구한 뒤, 만약 이 거리가 mid (=최소 거리) 보다 작다면 돌을 제거한다.

# 왜?? 우리는 현재 mid 변수의 값을 '문제의 정답'으로 설정한 뒤 풀고 있다.

# 만약 mid가 13일 때 0 과 2 사이의 거리는 2이고, 이는 우리가 설정한 정답(=mid)보다  작은 값이 된다.

# => 우리가 문제의 정답이라고 설정한 것에 위배된다! 정답은 최솟값인데 최솟값보다 더 작은 값이 있게 되는 것이니까!

# 4. 만약 3번 조건에 합당하지 않는다면 최소 거리를 갱신해준다. (정답에 더욱 가까우니까!)

# 5. 만약 지워야 하는 n보다 더 많이 돌을 지웠다면 우리가 설정한 최소거리(=mid)는 틀린 답이니까 이분 탐색의 범위를 좁혀준다.

# 여기서 중요!

# 6. 딱 n만큼 돌을 지웠거나 덜 지웠다면, 최솟값들 중 최댓값을 찾아야 한다!!

# 그래서 일단 정답을 저장해준 뒤, left를 증가시켜 범위를 높인 다음 최솟값에서 만족하지 않고 반대 방향으로 탐색하여 최솟값들 중 최댓값을 찾아준다.


def solution(distance, rocks, n):
    answer = 0

    rocks.append(distance)
    rocks = sorted(rocks)

    left, right = 0, distance

    while left <= right:

        mid = (left + right) // 2
        min_distance = float("inf")
        current = 0
        remove_cnt = 0

        for rock in rocks:
            diff = rock - current
            if diff < mid:
                remove_cnt += 1
            else:
                current = rock
                min_distance = min(min_distance, diff)

        if remove_cnt > n:
            right = mid - 1
        else:
            answer = min_distance
            left = mid + 1

    return answer


# 내가 풀어서 테케는 통과했지만 이분탐색으로 풀지 않아서 시간초과로 틀린 경우
from itertools import combinations
import copy


def solution(distance, rocks, n):
    rocks.sort()
    max_distance = 0
    for item in combinations(rocks, n):
        tmp_rocks = copy.deepcopy(rocks)
        for x in item:
            tmp_rocks.remove(x)
        tmp_rocks = [0] + tmp_rocks

        min_distance = 1e9
        for i in range(len(tmp_rocks) - 1):
            min_distance = min(min_distance, tmp_rocks[i + 1] - tmp_rocks[i])

        max_distance = max(max_distance, min_distance)

    return max_distance
