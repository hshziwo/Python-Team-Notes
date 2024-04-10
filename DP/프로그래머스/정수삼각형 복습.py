# triangle에 최대값을 누적시키면서 DP테이블처럼 이용해서 풀기
def solution(triangle):
    # 이전값을 참고하기 위해 1인덱스(2행)부터 시작
    for i in range(1, len(triangle)):
        prev = i - 1
        for j in range(len(triangle[i])):
            index_array = []
            # left
            if j - 1 >= 0:
                index_array.append(j - 1)
            # center
            if j < len(triangle[prev]):
                index_array.append(j)
            # right는 안됨 생각 잘해야함
            # prev가 있을 수 있는 상황은 left거나 바로 위의 center의 경우밖에 없음
            # if j + 1 < len(triangle[prev]):
            #     index_array.append(j + 1)

            value_array = []
            for index in index_array:
                prev_value = triangle[prev][index]
                value_array.append(triangle[i][j] + prev_value)

            # print(value_array)
            # 누적될 수 있는 값 중 최대값으로 DP테이블 갱신
            triangle[i][j] = max(value_array)

    # print(triangle)
    # 마지막 row에서 최대값을 리턴
    return max(triangle[-1])
