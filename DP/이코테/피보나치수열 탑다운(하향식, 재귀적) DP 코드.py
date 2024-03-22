dp_table = [0] * 100


def fibo(x):
    # 종료조건
    if x == 1 or x == 2:
        return 1

    # dp테이블에 값이 있으면 == 이미 계산한 문제면 바로 return하고 종료
    if dp_table[x] != 0:
        return dp_table[x]

    # 위에 종료조건을 만나거나 dp테이블값이 있을때까지 계속 점화식 재귀호출 하면서
    # dp테이블에 모든값 기입
    dp_table[x] = fibo(x - 1) + fibo(x - 2)

    # 계속 리턴되면서 맨 마지막은 처음 넣었던 x파라미터에 대한 값 여기서는 99에 대한 점화식 값을 리턴하게 됨
    return dp_table[x]


print(fibo(99))
