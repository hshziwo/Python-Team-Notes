# 백준 1676번: 팩토리얼 0의 개수 와 똑같은 문제인데
# 효율성에서 0점을 먹었다.
# python의 math.factorial이 성능이 안 좋나..
# https://www.acmicpc.net/problem/1676
# 해설
# https://trey-de.tistory.com/8

# 6번: 팩토리얼값의 뒤 0의 개수를 구하는 건데 python의 기본 내장함수 math.factorial(n)을 해서 효율성이 0점 나왔다.
# 5의 개수를 누적합으로 구하는 풀이가 있다고 한다.

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
