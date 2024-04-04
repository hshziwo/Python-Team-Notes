# 리스트 안에 있는 인용 횟수에 포함되지 않은 값이 h의 값이 될 수도 있다고 깨달았습니다
# 결국 못 풀었음
# 정답 보니까 그냥 내림차순 정렬하고 h_index를 카운팅 하니까 정답임...
def solution(citations):
    citations.sort(reverse=True)
    h_index = 0
    for c in citations:
        if c > h_index:
            h_index += 1
    return h_index
