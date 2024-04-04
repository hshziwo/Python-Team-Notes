# 예전에 푼거
# 이게 더 나은 듯
def solution(answers):
    number_one = [1, 2, 3, 4, 5]
    number_two = [2, 1, 2, 3, 2, 4, 2, 5]
    number_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    one = 0
    two = 0
    three = 0
    for i in range(len(answers)):
        if answers[i] == number_one[i % 5]:
            one += 1
        if answers[i] == number_two[i % 8]:
            two += 1
        if answers[i] == number_three[i % 10]:
            three += 1

    tmp = [one, two, three]
    max_value = max(tmp)
    answer = [i + 1 for i in range(len(tmp)) if max_value == tmp[i]]
    return answer


# 비슷한데 좀 비효율적으로 푼거
def solution(answers):
    answer = []
    first = 0
    second = 0
    third = 0
    first_answer = [1, 2, 3, 4, 5]
    second_answer = [2, 1, 2, 3, 2, 4, 2, 5]
    third_answer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == first_answer[i % 5]:
            first += 1
        if answers[i] == second_answer[i % 8]:
            second += 1
        if answers[i] == third_answer[i % 10]:
            third += 1

    max_value = max(first, second, third)
    if first == max_value:
        answer.append(1)
    if second == max_value:
        answer.append(2)
    if third == max_value:
        answer.append(3)
    return answer
