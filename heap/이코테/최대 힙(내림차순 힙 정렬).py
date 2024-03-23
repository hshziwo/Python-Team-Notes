import heapq


# 파이썬에서 최대힙을 쓰려면 기존 최소힙에 부호를 -로 넣고 -로 빼면 된다.


# 내림차순 힙 정렬
def heapsort(iterable):
    h = []
    result = []

    # 힙에 담기
    for value in iterable:
        heapq.heappush(h, -value)  # -value로 넣기

    for i in range(len(h)):
        result.append(
            -heapq.heappop(h)
        )  # -넣어서 부호 다시 복구하면 큰수부터 나와서 담긴다.

    return result


result = heapsort([1, 5, 3, 2, 6])
print(result)
