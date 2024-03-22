import sys

input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

array1.sort()
array2.sort(reverse=True)
for i in range(k):
    if array1[i] < array2[i]:
        array1[i], array2[i] = array2[i], array1[i]
    else:
        # array1이 크거나 같으면 이후에는 바꿀 필요없음
        break

print(sum(array1))
