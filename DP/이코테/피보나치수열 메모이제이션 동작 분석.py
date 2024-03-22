dp_table = [0] * 100


def fibo(x):
    print(f"f({str(x)})", end=" ")

    if x == 1 or x == 2:
        return 1

    if dp_table[x] != 0:
        return dp_table[x]

    dp_table[x] = fibo(x - 1) + fibo(x - 2)

    return dp_table[x]


fibo(6)
