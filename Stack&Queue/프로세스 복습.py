# 테스트케이스
# 입력값 〉 [5, 4, 3, 2, 1], 4
# 기댓값 〉 5
# 이걸 예외처리 해줘야함.
# 아래 주석 단거 확인

def solution(priorities, location):
    queue = [i for i in range(len(priorities))]
    count = 0
    while queue:
        index = queue.pop(0)
        value = priorities[index]
        
        # 여기서 queue가 비었는 지 먼저 확인을 해줘야 에러가 안남
        if queue and value < max([priorities[i] for i in queue]):
            queue.append(index)
            continue
            
        count += 1
        
        if index == location:
            return count

    return count