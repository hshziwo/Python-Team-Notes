# 연습문제 2번과 같음
# 성적이 배열로 주어질 때 각 성적의 등수를 배열로 반환, 동점은 같은 등수로 처리하고 그 다음 등수는 + 동점자수
# 문제 그대로 동점은 같은 등수로 처리하고 그 다음 등수는 이전 등수 + 이전 동점자수 + 1(next의 의미)


def solution(grade):
    sorted_grade = sorted(grade, reverse=True)
    grade_rank = {}
    cur_rank = 0
    same_rank = 0
    for i in sorted_grade:
        if i not in grade_rank:
            cur_rank = cur_rank + same_rank + 1
            same_rank = 0
            grade_rank[i] = cur_rank
        else:
            grade_rank[i] = cur_rank
            same_rank += 1

    answer = []
    for i in grade:
        answer.append(grade_rank[i])

    return answer
