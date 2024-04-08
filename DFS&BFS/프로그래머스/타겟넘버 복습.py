# DFS로 모든 numbers에 대해 가지치는 방법으로 해결함
def dfs(index, numbers, target, count, start):
    # 마지막에 도달하면 무조건 종료
    if index == len(numbers):
        if target == start:
            # target과 동일할 경우 count를 +1 해서 돌려줌
            count += 1
        return count

    # -와 +의 경우
    array = [-numbers[index], numbers[index]]
    index += 1
    for number in array:
        # 현재 누적된 값이 -경우와 +경우에 대해 각각 가지를 쳐야 하므로 tmp_target 사용
        tmp_target = start
        tmp_target += number
        count = dfs(index, numbers, target, count, tmp_target)

    return count


def solution(numbers, target):
    return dfs(0, numbers, target, 0, 0)


# 정답에 있는 간단하게 짠 코드
# 근데 이렇게 구현하라면 바로 생각이 안날듯
def solution(numbers, target):

    def calc(idx, sum):
        nonlocal answer

        if idx == len(numbers):
            if sum == target:
                answer += 1
            return

        calc(idx + 1, sum + numbers[idx])
        calc(idx + 1, sum - numbers[idx])

    answer = 0
    calc(0, 0)

    return answer
