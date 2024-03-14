n = int(input())
array = list(map(int, input().split()))

count = 0
array = sorted(array)
index = 0
while True:
    next_index = index + array[index] - 1
    if next_index < len(array) and array[index] == array[next_index]:
        count += 1
        index = next_index + 1
    else:
        break

print(count)