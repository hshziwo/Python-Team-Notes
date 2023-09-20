n, k = map(int, input().split())

count = 0

while True :
  # 한번에 k 나누기까지 도달
  # n-1의 역할들 한번에
  target = (n // k) * k
  count += (n - target)
  n = target

  if n < k :
    break

  #k로 나누기
  count += 1
  n //= k

# n < k 의 조건에서 1까지만 남기고 도달한 수를 count에 더해주기
count += (n -1)
print(count)