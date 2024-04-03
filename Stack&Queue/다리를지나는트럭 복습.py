# 못 풀었음 그냥 정답 보고 해석함
def solution(bridge_length, weight, truck_weights):
    # 일단 다리 길이 만큼의 배열을 만들어서 트럭이 위치할 수 있는 다리 배열을 만든다.
    # 큐라고 생각하고
    # 초기에는 0kg짜리 트럭이 다리 길이 갯수만큼 있다고 생각
    q = [0] * bridge_length
    sec = 0
    total = 0
    # 모든 트럭이 지나갈 때까지
    while q:
        sec += 1
        # 1초가 지나면 트럭하나가 나갔다고 생각
        total -= q.pop(0)

        # 실제 트럭이 있을 때
        if truck_weights:
            # 현재 다리 위의 트럭의 kg와 진입해볼 트럭의 합이 다리가 버티는 무게보다 작거나 같을때
            # if sum(q)+truck_weights[0]<=weight:
            # sum(q)을 쓰면 효율성을 통과 못함. while문 밖에서 totald을 계산하는 식으로 개선
            if total + truck_weights[0] <= weight:
                # 다리에 올림
                truck_weight = truck_weights.pop(0)
                q.append(truck_weight)
                total += truck_weight
            else:
                # 아니라면 한 트럭이 끝날때까지 기다려야 하므로 0을 넣어서 while문이 계속 돌아 대기할 수 있도록 함
                # 이 부분이 중요
                q.append(0)
    return sec


# import collections
# def solution(bridge_length, weight, truck_weights):
#     q = collections.deque([0] * bridge_length)
#     truck_weights = collections.deque(truck_weights)
#     sec = 0
#     total = 0
#     while q:
#         sec += 1
#         qq = q.popleft()
#         total -= qq
#         if truck_weights:
#             if total + truck_weights[0] <= weight:
#                 truck = truck_weights.popleft()
#                 total += truck
#                 q.append(truck)
#             else: q.append(0)

#     return sec
