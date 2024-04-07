# 이건 수학 문제라... 애매함
# 정확한 정답은 정답 파일에 있음
def solution(brown, yellow):
    # 전체합의 최대공약수를 구하는 걸로 생각함.
    total = brown + yellow
    width = 0
    height = 0
    # 가로 1부터 시작해서 max는 brown수로 생각
    for i in range(1, brown + 1):
        # 최대공약수가 아니면 넘김
        if total % i != 0:
            continue
        else:
            remain = brown - (i * 2)
            # brwon에서 가로의 2배를 빼고
            # 반으로 나눈 후 위아래 블록(+2)를 더해주면 한쪽 세로길이가 나온다고 생각함.
            tmp_height = (remain / 2) + 2
            # 가로와 세로의 곱이 total의 최대공약수일떄
            # 가로의 길이가 항상 기므로 계속 상위로 갱신 해줌.
            if total == (i * tmp_height):
                width = i
                height = tmp_height

    # 마지막으로 갱신된 가로 세로를 리턴
    return [width, height]
