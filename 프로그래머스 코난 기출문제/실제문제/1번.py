# [프로그래머스] 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 해설
# https://a-littlecoding.tistory.com/85

# 1번 : 중복제거 문제, enumerate를 쓰고 싶어서 마지막 인덱스 일때는 IndexError가 나서 try except로 처리해서 마지막꺼를 넣어줬다.


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
