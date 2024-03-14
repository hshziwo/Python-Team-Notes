n = int(input())
data = list(map(int, input().split()))

data.sort()

result = 0
count = 0
for i in data :
  count += 1
  #현재 포함된 카운트가 그룹만들수 있는지
  if count >= i :
    result += 1
    count = 0

print(result)