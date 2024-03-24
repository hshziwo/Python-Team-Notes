# 연습문제 3번과 같음
# 그리디 문제
# 비슷한 문제 백준 14916번 - 거스름돈
# https://www.acmicpc.net/problem/14916
# 해설
# https://devjeong.com/algorithm/algorithm-4/


def solution(n):
    answer = 0

    while n > 0:
        # 5로 나눠질때까지 -3을 빼주면서 카운팅하고 5로 나눠지는 순간 나눌 수 있는 몫을 카운트에 더하고 멈추면 정답
        if n % 5 == 0:
            answer += n // 5
            break
        else:
            n -= 3
            answer += 1

    if n < 0:
        return -1
    else:
        return answer
