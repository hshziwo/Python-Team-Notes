# 못 풀어서 정답 보고 다시 품
# 진입이 아니라 진출 시점으로 문제를 푸는 것이 핵심
# queue라고 생각하고 순차적으로 popleft해야함
def solution(routes):
    count = 0
    # 진출 값 기준으로 오름차순 정렬
    routes.sort(key=lambda x: x[1])
    while routes:
        value = routes[0][1]
        while True:
            # 진입 시점이 현재 진출값보다 작은 차량
            # 즉, 현재 카메라 위치보다 먼저 들어왔던 차들은 popleft 해줌
            if routes and routes[0][0] <= value:
                routes.pop(0)
            else:
                break
        # 한 번 순회하면 그 장소에 카메라 한대가 있다는 뜻이므로
        # count를 1 증가시킴
        count += 1
    return count
