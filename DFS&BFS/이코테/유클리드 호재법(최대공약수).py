# greatest common divisor(최대공약수)
# 마지막에 나눠서 나머지가 0이 되는 값이 최대공약수
# 수학적 원리임
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print(gcd(192, 162))
