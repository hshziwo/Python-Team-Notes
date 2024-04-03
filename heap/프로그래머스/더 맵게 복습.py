# 이거는 다른 사람이 푼건데 비슷하게 풀었으나 정리가 깔끔하게 되어 있어 퍼옴
import heapq as hq


def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second * 2)
        answer += 1

    return answer


# 이거는 내가 푼 거
import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    check = False
    while scoville:
        # 이미 모두 K보다 클때는 바로 0 리턴
        if scoville[0] >= K:
            return count

        if len(scoville) < 2:
            break

        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        if a >= K:
            check = True
            break

        heapq.heappush(scoville, (a + (b * 2)))
        count += 1

    if check == True:
        return count
    else:
        return -1
