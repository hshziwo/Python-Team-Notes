# 사실상 문제를 보면 가로x세로 길이를 명시해서 더 헷갈리게 만들었다.
# 사실 어떤 모서리는 가로가 될 수도 있고 세로도 될 수가 있다.
# 그치만 한 모서리를 가로라고 지정하면 다른 모서리는 세로가 되어야 옳다.

# 두 개의 모서리를 비교하여 큰 값을 전부 가로 작은 값을 전부 세로로 두면
# 각 모서리의 길이의 최댓값이 답이 되지않을까?


def solution(sizes):
    row = 0
    column = 0
    for size in sizes:
        if size[0] > size[1]:
            row = max(row, size[0])
            column = max(column, size[1])
        else:
            row = max(row, size[1])
            column = max(column, size[0])

    return row * column
