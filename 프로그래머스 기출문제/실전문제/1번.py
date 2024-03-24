# [프로그래머스] 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 해설
# https://a-littlecoding.tistory.com/85


def solution(arr):
    answer = []

    for i, v in enumerate(arr):
        try:
            if v != arr[i + 1]:
                answer.append(v)
        except IndexError:
            answer.append(v)
    return answer


# 예전에 내가 푼거
def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0 or answer[len(answer) - 1] != i:
            answer.append(i)

    return answer
