def solution(bridge_length, weight, truck_weights):
    answer = 1
    wait_truck = []
    
    while truck_weights :
        cur = truck_weights.pop(0)
        
        while True :
            if sum(wait_truck) + cur <= weight :
                if len(wait_truck) > 0 :
                    answer += 1
                wait_truck.append(cur)
                break
            else :
                wait_truck.pop(0)
                if len(wait_truck) == 0 :
                    answer += bridge_length
    
    if len(wait_truck) > 0 :
        answer += bridge_length
        
    return answer




def solution(bridge_length, weight, truck_weights):
    answer = 0
    wait_truck = []
    
    while truck_weights :
        cur = truck_weights.pop(0)
        
        
        while True :
            if sum(wait_truck) + cur <= weight :
                answer += 1
                wait_truck.append(cur)
                break
            else :
                wait_truck.pop(0)
                if len(wait_truck) == 0 :
                    answer += bridge_length
    
    if len(wait_truck) > 0 :
        answer += bridge_length
        
    return answer


def solution(bridge_length, weight, truck_weights):
    answer = 1
    wait_truck = []
    while truck_weights :
        truck = truck_weights.pop(0)
        
        while True :
            if len(wait_truck) == 0 :
                wait_truck.append(truck)
                break
            elif sum(wait_truck) + truck <= weight :
                wait_truck.append(truck)
                answer += 1
                break
            else :
                wait_truck.pop(0)
                if len(wait_truck) == 0 :
                    answer += bridge_length
                
    if len(wait_truck) > 0 :
        answer += bridge_length
    return answer


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length

    while truck_weights :
        bridge.pop(0)
        
        if sum(bridge) + truck_weights[0] <= weight :
            truck = truck_weights.pop(0)
            bridge.append(truck)
        else :
            bridge.append(0)

        answer += 1

    answer += bridge_length

    return answer