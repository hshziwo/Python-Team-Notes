def solution(n, lost, reserve):
    # set을 쓰면 미리 sort로 정렬할 필요없이 자동으로 오름차순 정렬됨
    real_lost = list(set(lost) - set(reserve))
    real_reserve = list(set(reserve) - set(lost))

    # real_lost 빼고 모두 체육복이 있다고 가정
    visited = [True if i not in real_lost else False for i in range(n + 1)]
    # 0번째는 이 문제에는 없는 번호여서 False처리
    # 이 문제는 1부터 시작하기 때문에 이렇게 이용함.
    visited[0] = False

    for index in real_lost:
        if not real_reserve:
            break

        left = index - 1
        right = index + 1
        if left > 0 and left in real_reserve:
            visited[index] = True
            real_reserve.remove(left)
        elif right < len(visited) and right in real_reserve:
            visited[index] = True
            real_reserve.remove(right)

    return visited.count(True)
