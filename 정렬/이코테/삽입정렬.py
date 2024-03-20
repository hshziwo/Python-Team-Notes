array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 0인덱스가 아니라 1인덱스부터 시작해서 계속 왼쪽의 값들과 비교해야함
for i in range(1, len(array)):
    # 현재의 위치 i에서 왼쪽에 이미 정렬된 값들을 역순으로(-1) 가면서 현재값과 비교해서 작으면 바꿔준다(오름차순 일때)
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            # 아니면 멈춤
            break

print(array)
