n = int(input())
array = list(map(int, input().split()))

max_count = 0

for i in range(n) :
    first_val = array[i]
    sum_val = 0

    for j in range(i+2, n) :
        sum_val = first_val + array[j]

        if first_val > sum_val :
            sum_val = first_val

        if max_count < sum_val :
            max_count = sum_val

print(max_count)
