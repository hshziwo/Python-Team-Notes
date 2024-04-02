# 고것은 한 장르에 무조건 두개 이상 곡이 수록되어 있지 않다는 것
# 사이트에서 장르별로 가장 많이 재생된 두곡 이라고 하면 두곡 이상 있어 보이잖아 하지만 제한사항에 장르에 속한 곡이 하나면 하나만 선택합니다. 라고 되어있다.
# 그래서 예외처리를 따로 잘 해줘야 한다.
# 조건 3번을 보면
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

# 다시 말해서 하나의 정렬조건으로 구현하면 안된다.
# 나는 재생횟수가 많은 노래를 정렬하려고 했어서..
# findAll에 대한 람다함수가 필요하다.


# 내가 푼건데 통과하긴 했는데 좀 이상함
def solution(genres, plays):
    hash_table = {}
    for i in range(len(genres)):
        if genres[i] not in hash_table:
            hash_table[genres[i]] = [plays[i]]
        else:
            hash_table[genres[i]].append(plays[i])

    value_table = {}
    for key, value in hash_table.items():
        value_table[sum(value)] = key

    sorted_table = sorted(list(map(int, value_table.keys())), reverse=True)
    answer = []
    for value in sorted_table:
        play = hash_table[value_table[value]]
        play.sort(reverse=True)
        count = 2
        if len(play) < 2:
            count = len(play)

        for i in range(count):
            check = False
            # findAll에 대한 람다함수
            array = list(filter(lambda x: plays[x] == play[i], range(len(plays))))
            for j in array:
                if check == False and j not in answer:
                    check = True
                    answer.append(j)
    return answer
