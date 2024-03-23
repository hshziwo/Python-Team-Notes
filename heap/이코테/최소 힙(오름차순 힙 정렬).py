import heapq


# 오름차순 힙 정렬
def heapsort(iterable):
    h = []
    result = []

    # 힙에 담기
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에서 오름차순 우선순위대로 뽑기
    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result


result = heapsort([1, 5, 3, 2, 6])
print(result)
