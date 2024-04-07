from itertools import permutations
import math


# 소수 체크 함수
# math.sqrt로 절반만 체크하는 것이 엄청난 효율을 보여준다
# 소수 찾기는 꼭 이걸로 해야함.
# 이코테의 소수 판별 코드를 꼭 복습하기
# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    # 제곱근까지만 확인하는 개선된 버전
    # 무조건 제곱근 방법을 써야 성능이 나옴
    # 여기서 x를 제곱근까지만(==제곱근 + 1) for문에서  체크하기 때문에
    # 2, 3 같은 작은 소수라도 아예 for문을 돌지 않고 바로 True를 리턴해서
    # 소수 판별 함수가 성립한다.

    # 1이하 값 바로 False
    # 처리 안해주면 로직상 True됨
    if x < 2:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님

    return True  # 소수임


def solution(numbers):
    set_array = set([])
    number_array = list(numbers)
    for i in range(1, len(number_array) + 1):
        array = permutations(number_array, i)
        for item in list(array):
            value = int("".join(item))
            # 소수는 0과 1 그리고 자기 자신을 제외한 수에 대해서 나눠지면 안됨
            if is_prime_number(value):
                set_array.add(value)

    return len(set_array)
