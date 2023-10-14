def solution(answers):
    number_one = [1,2,3,4,5]
    number_two = [2,1,2,3,2,4,2,5]
    number_three = [3,3,1,1,2,2,4,4,5,5]
    
    one = 0
    two = 0
    three = 0
    for i in range(len(answers)) :
        if answers[i] == number_one[i%5] :
            one += 1
        if answers[i] == number_two[i%8] :
            two += 1
        if answers[i] == number_three[i%10] :
            three += 1
    
    tmp = [one,two,three]
    max_value = max(tmp)
    answer = [i+1 for i in range(len(tmp)) if max_value == tmp[i]]
    return answer