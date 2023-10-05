# // 핵심은 나머지 작업이 기다리는 시간의 합을 최소화 해야 함
# // 현재 처리 가능한 요청 중에서 가장 짧은 작업시간을 우선 처리하면 나머지 작업이 기다리는 시간이 줄어든다.
# // jobs를 요청 시간 순으로 정렬하고, 현재 시간과 비교하여 시작이 가능한 순간에 우선순위 큐에 삽입한다.
# // 우선순위 정렬은 짧은 작업시간으로 한다.
# // 작업이 끝나면 우선순위 큐의 첫번째 작업을 시작한다.
# // 반복


import heapq
def solution(jobs):    
    tmp_heap = []
    for i in jobs :
        heapq.heappush(tmp_heap, (i[1], i))
        
    answer = 0
    count = tmp_heap[0][1][0]
    while tmp_heap :
        value = heapq.heappop(tmp_heap)
        wait_value = count - value[1][0]
        work_value = value[1][1]
        count += work_value
        answer += wait_value + work_value
        
    answer = answer // len(jobs)
    return answer

# 테스트 케이스
# [[0, 3], [10, 1]] => 2
# [[7, 8], [3, 5], [9, 6]] => 9
# [[1, 4], [7, 9], [1000, 3]] => 5
# [[0, 1], [2, 2], [2, 3]] => 2





# // 핵심은 나머지 작업이 기다리는 시간의 합을 최소화 해야 함
# // 현재 처리 가능한 요청 중에서 가장 짧은 작업시간을 우선 처리하면 나머지 작업이 기다리는 시간이 줄어든다.
# // jobs를 요청 시간 순으로 정렬하고, 현재 시간과 비교하여 시작이 가능한 순간에 우선순위 큐에 삽입한다.
# // 우선순위 정렬은 짧은 작업시간으로 한다.
# // 작업이 끝나면 우선순위 큐의 첫번째 작업을 시작한다.
# // 반복

import heapq
def solution(jobs):    
    tmp_heap = []
    for i in jobs :
        heapq.heappush(tmp_heap, (i[1], i))
    
    answer = 0
    second = 0
    disk = []
    while tmp_heap :
        if len(disk) == 0 :
            value = heapq.heappop(tmp_heap)
            disk.append(value[1])
            wait_value = second - value[1][0]
            work_value = value[1][1]
            second += work_value
            answer += wait_value + work_value
            disk.pop(0)
        else :
            second += 1
        
    answer = answer // len(jobs)
    return answer