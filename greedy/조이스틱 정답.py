def solution(name):

	# 조이스틱 조작 횟수 
    answer = 0
    
    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1
    
    for i, char in enumerate(name):
    	# 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        # 일단 i는 현재 index를 찾은 다음 수행임
        # next는 현재 index 기준에서 연속된 마지막 A의 인덱스로 next를 옮김 이것 때문에 남은 길이를 구할 수 있음.
        # 좌측은 현재 온만큼 돌아갈 꺼기 때문에 현재 인덱스에 2배하고 남은 길이(len(name) - next)를 더함
        # 우측은 우측으로 왔다갔다한 길이(len(name) -next)]) 더하기 왼쪽의 남은 길이(i)를 더한것임
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
        
    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer