n = int(input())
x_array = list(map(int, input().split()))

x_array.sort(reverse=True)

count = 0
for i in range(len(x_array)) :
  n = n - x_array[i]

  if n >= 0 :
    count +=1
  else :
    break

print(count)