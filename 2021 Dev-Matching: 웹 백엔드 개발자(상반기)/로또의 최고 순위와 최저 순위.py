def solution(lottos, win_nums):
    zero_count = 0
    correct_count = 0
    for x in lottos :
        if x == 0 :
            zero_count += 1
        if x in win_nums :
            correct_count += 1
            
    best_rank = abs(zero_count + correct_count - 7) 
    if best_rank > 6 :
        best_rank = 6
    worst_rank = abs(correct_count - 7) 
    if worst_rank > 6 :
        worst_rank = 6
    return [best_rank, worst_rank]