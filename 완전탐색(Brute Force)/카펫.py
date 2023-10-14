# 팁
# [18, 6] -> [8, 3] (o)
# [18, 6] -> [6, 4] (x)

def solution(brown, yellow):
    answer = []
    count = int(brown) + int(yellow)
    for i in range(1, count + 1) :
        if count % i == 0 :
            x = i
            y = count // i
            condition = x * 2 + (y - 2) * 2
            if condition == brown and x >= y :
                answer.append(x)
                answer.append(y)
                break
    return answer