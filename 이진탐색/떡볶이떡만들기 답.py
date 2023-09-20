n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result =0
while start <= end :
    total = 0
    mid = (start + end) // 2
    
    for x in array :
        if x > mid:
            total += x - mid
           
    if total < m:
        end = mid - 1
    # total이 m 보다 크거나 같으면
    # 같을때는 마지막 최종임
    else:
        result = mid
        start = mid +1

print(result)