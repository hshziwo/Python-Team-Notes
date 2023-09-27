def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    total_weight = 0

    while truck_weights :
        total_weight -= bridge.pop(0)
        
        if total_weight + truck_weights[0] <= weight :
            truck = truck_weights.pop(0)
            bridge.append(truck)
            total_weight += truck
        else :
            bridge.append(0)

        answer += 1

    answer += bridge_length

    return answer