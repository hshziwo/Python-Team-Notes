import math


# 소수 판별 함수
def is_prime_number(x):
    # 1이하 값 바로 False
    # 처리 안해주면 로직상 True됨
    if x < 2:
        return False

    # 2부터 (x - 1)까지의 모든 수를 확인하는
    # x - 1까지만 확인하기 위해 range를 x까지로 설정함
    # 여기서 함수가 (자기자신 - 1)까지만 for을 돌기 때문에 2,3 같은 걸 소수로 판별할 수 있음
    # 예를 들어 2는 1까지만 for문을 돌고 3은 2까지만 for문을 돌기 떄문에 for문을 넘어가고 바로 True 리턴
    # 일반버전
    # for i in range(2, x):

    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    # 제곱근까지만 확인하는 개선된 버전
    # 무조건 제곱근 방법을 써야 성능이 나옴
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


print(is_prime_number(2))  # 2은 소수임
print(is_prime_number(4))  # 4는 소수가 아님
print(is_prime_number(7))  # 7은 소수임
