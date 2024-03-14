n = int(input())
array = list(map(int, input().split()))

array = sorted(array)
count = 0
index = 0
while True :
    next_index = index + array[index]
    if next_index < len(array) and array[index] == array[next_index] :
        count += 1
        index = next_index + 1
    # else 

    if next_index > len(array) :
        break

print(count)
