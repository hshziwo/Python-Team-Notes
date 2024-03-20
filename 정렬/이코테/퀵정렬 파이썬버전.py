array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


# 리스트 컨프리헨션 이용
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]  # 피벗
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    # 분할 된 이후 왼쪽 오른쪽 부분 재귀 돌면서 정렬 수행
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
