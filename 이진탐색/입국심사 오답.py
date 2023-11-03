def solution(n, times):
    def binary_search(start, end) :
        if start >= end :
            return start
        mid = (start + end) // 2
        value = sum([mid // x for x in times])
        if n == value :
            return mid
        elif n > value :
            # 덜 처리됨
            # mid 오른쪽에서 시작
            return binary_search(mid+1, end)
        else :
            # 더 처리됨
            # mid 왼쪽까지 처리
            return binary_search(start, mid-1)
    answer = binary_search(0, 1000000000)
    return answer


def solution(n, times):
    start, end = 1, 1000000000
    
    while start < end :
        mid = (start + end) // 2
        value = sum([mid // x for x in times])
        
        if n == value :
            start = mid
            break
        elif n > value :
            # 덜 처리됨
            # 우측부터 시작
            start = mid + 1
        else :
            # 많이 처리됨
            # 좌측까지 조정
            end = mid - 1
    answer = start
    return answer