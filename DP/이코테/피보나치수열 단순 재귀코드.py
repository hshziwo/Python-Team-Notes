def fibo(x):
    if x == 1 or x == 2:
        # 맨 처음 시작인 1 + 1 처리
        # 즉 재귀 종료 조건임
        # 피보나치 수열 : 1 + 1 + 2 + 3 ~~~
        return 1

    # 재귀 호출
    return fibo(x - 1) + fibo(x - 2)


print(fibo(4))
