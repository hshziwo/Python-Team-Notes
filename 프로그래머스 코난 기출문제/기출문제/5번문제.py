# 특정 숫자를 이진수로 바꾸어 그 숫자보다 작은 수들중 이진수로 바꾸었을 때 1의 갯수가 똑같은 수의 갯수
# 비슷한 문제 [프로그래머스 Level2] 다음 큰 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12911
# https://velog.io/@falling_star3/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level2-%EB%8B%A4%EC%9D%8C-%ED%81%B0-%EC%88%AB%EC%9E%90

def check(num) :
    binary = bin(num)
    count = binary.count('1')
    return count

def solution5(num) :
    count = check(num)

    answer = 0
    for i in range(num) :
        if check(i) == count :
            answer += 1

    return answer

print(solution5(4))