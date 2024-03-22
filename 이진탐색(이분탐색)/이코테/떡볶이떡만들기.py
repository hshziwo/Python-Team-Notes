n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort(reverse=True)

max_value =array[0]
max_count = 0

for i in range(max_value, 0, -1) :
    sum = 0
    for j in range(n) :
        if array[j] <= i :
            break

        tmp = array[j] - i
        
        if tmp > 0 :
            sum += tmp

    if sum == m :
        max_count = i
        break

print(i)

