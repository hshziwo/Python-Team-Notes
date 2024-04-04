# 다시 해도 못풀어서 그냥 정답의 내용을 해석하기로 함
import heapq


def solution(jobs):
    answer, now, i = 0, 0, 0
    start = (
        -1
    )  # -1부터 시작인 이유는 0초 일때 시작해야 하는 프로세스부터 heap 담기 위해서임
    heap = []

    while i < len(jobs):
        for j in jobs:
            # j[0] == 프로세스가 원래 시작해야할 시간
            # 프로세스가 시작해야 할 시간이 start(이전 now)보다 크고 현재 now 보다 작거나 같으면
            # (== 시작했어야 했으나 대기하거나 아니면 지금 딱 시작해야하는 경우)
            # heap에 (비용, 시작시간) 으로 넣어줘서 min heap을 만들어줌
            # 이때 while문이 0부터 len(jobs) 까지 돌기 떄문에 for문은 매 인덱스마다 시간을 체크해서 조건을 만족하면 heap에 넣어줌
            if start < j[0] <= now:
                heapq.heappush(heap, (j[1], j[0]))

        # heap이 존재할때
        if heap:
            # min heap이므로 최소 수행시간순으로 pop됨
            current = heapq.heappop(heap)
            # heap에서 꺼냈으면 현재시간을 start에 넣고
            # (시작시간을 현재 시간으로 당긴다는 뜻)
            start = now
            # 현재시간은 현재 프로세스의 수행시간(current[0])을 더해준다
            # 현재 pop으로 꺼낸 프로세스가 수행완료한 시간으로 만들어줌
            now += current[0]
            # 실제 문제에서는 현재 프로세스가 수행한 실제 수행시간인
            # 프로세스가 대기한 시간까지 더해야하므로
            # (현재시간 - 원래 시작했어야 할 시간(current[1])) == 실제 대기 + 걸린 시간
            # 으로 값을 구해 answer에 누적해준다.
            answer += now - current[1]

            # len(job)만큼 반복한다.
            i += 1
        else:
            # 조건에 맞는 heap이 현재 없으면 현재 시간을 1초 늘려준다.
            now += 1

    # 평균 수행시간을 return
    return answer // len(jobs)
