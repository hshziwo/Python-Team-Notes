def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    real_lost = [i for i in lost if i not in reserve]
    count = n - len(real_lost)
    if len(lost) == 0 :
        return n
    elif len(reserve) == 0 :
        return count
    visited = [i for i in range(1,n+1) if i not in real_lost]
    for i in reserve :
        if i in lost :
            continue
        prev_index = i - 1
        next_index = i + 1
        if prev_index in lost and prev_index not in visited:
            count += 1
            visited.append(prev_index)
        elif next_index in lost and next_index not in visited:
            count += 1
            visited.append(next_index)
            
    return count