# 두명의 사람이 쿠키가 담긴 바구니를 왼쪽, 오른쪽에서 부터 각각 먹기 시작할 때 똑같은 갯수를 먹을 수 있을 때의 최대 쿠키 갯수
# https://school.programmers.co.kr/learn/courses/30/lessons/49995
# 해설
# https://deok2kim.tistory.com/125


def solution(cookie):
    answer = 0
    n = len(cookie) - 1

    for i in range(n):
        left_sum, left_idx = cookie[i], i
        right_sum, right_idx = cookie[i + 1], i + 1

        while True:
            if left_sum == right_sum:
                answer = max(answer, left_sum)
                # answer = max(answer, right_sum)

            if left_idx > 0 and left_sum <= right_sum:
                left_idx -= 1
                left_sum += cookie[left_idx]
            elif right_idx < n and right_sum <= left_sum:
                right_idx += 1
                right_sum += cookie[right_idx]
            else:
                break

    return answer
