# 연습 5번이랑 같은데 5.4점 나옴
# 효율성이 0점

# 2번: bin함수로 이진수로 바꿔 .count(‘1’)함수로 1의 수를 세는 방식으로 했는데 효율성이 0점 나왔다.


def solution(num):
    count = bin(num).count("1")

    answer = 0
    for i in range(num):
        if bin(i).count("1") == count:
            answer += 1

    return answer


# 연습문제 5번 풀이 방법
# 근데 이것도 효율성 0점
def check(num):
    binary = bin(num)
    count = binary.count("1")
    return count


def solution(num):
    count = check(num)

    answer = 0
    for i in range(num):
        if check(i) == count:
            answer += 1

    return answer
