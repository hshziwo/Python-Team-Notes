# 백준 1676번: 팩토리얼 0의 개수 와 똑같은 문제인데
# 효율성에서 0점을 먹었다.
# python의 math.factorial이 성능이 안 좋나..
# https://www.acmicpc.net/problem/1676
# 해설
# https://trey-de.tistory.com/8

import math


def solution(n):
    n_factorial = str(math.factorial(n))
    cnt = 0

    for i in range(len(n_factorial) - 1, -1, -1):
        if n_factorial[i] == "0":
            cnt += 1
        else:
            break

    return cnt


# 팩토리얼 함수를 직접 구현한 거
def solution(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    fact_list = list(str(fact))

    fact_list_len = len(fact_list)

    cnt = 0

    for i in range(len(fact_list)):
        if fact_list[fact_list_len - 1 - i] != "0":
            break
        elif fact_list[fact_list_len - 1 - i] == "0":
            cnt = cnt + 1

    return cnt
