array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1  # 피봇 오른쪽부터 시작
    right = end
    while left <= right:  # 교차하면 중지
        # 피벗보다 큰 값을 찾을 때까지
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 값을 찾을 때까지
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 교차 됐다면 right가 작은 값이기 떄문에 right값과 pivot값 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            # 아니면 left right값 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분 각각 재귀적으로 계속 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
