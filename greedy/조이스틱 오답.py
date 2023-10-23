#첫번째 오답
def forward(name) :
    total = 0
    for i,text in enumerate(name) :
        count = 0 # A일때
        alphabet = ord(text)
        if alphabet != 65 :
            condition = 78
            if alphabet <=condition :
                for j in range(66, 91) :
                    count += 1
                    if alphabet == j :
                        break
            else :
                for j in range(90, 65, -1) :
                    count += 1
                    if alphabet == j :
                        break
        elif len(name) == 3 and i == 1 :
            continue
            
        if i != len(name) - 1 :
            count += 1
            
        total += count
    return total

def backward(name) :
    total = 0
    for i in range(0, -len(name), -1) :
        count = 0 # A일때
        alphabet = ord(name[i])
        if alphabet != 65 :
            condition = 78
            if alphabet <=condition :
                for j in range(66, 91) :
                    count += 1
                    if alphabet == j :
                        break
            else :
                for j in range(90, 65, -1) :
                    count += 1
                    if alphabet == j :
                        break
        elif len(name) == 3 and i == -1 :
            continue
            
        if i != -len(name) + 1 :
            count += 1
            
        total += count
    return total


def solution(name):
    # "A" = 65
    # "Z" = 90
    answer_foward = forward(name)
    answer_backward = backward(name)

    return min(answer_foward,answer_backward)


# 2번째 오답
def forward(name) :
    total = 0
    last_idx = len(name) - 1
    for i,text in enumerate(name) :
        alphabet = ord(text)
        if alphabet != 65 :
            condition = 78
            if alphabet <= condition :
                for j in range(66, 91) :
                    total += 1
                    if alphabet == j :
                        break
            else :
                for j in range(90, 65, -1) :
                    total += 1
                    if alphabet == j :
                        break
        value = True
        for tmp in name[i+1:last_idx + 1] :
            if tmp != "A" :
                value = False
                break
        if value == True :
            break    

        total += 1    
    return total

def backward(name) :
    total = 0
    last_idx = -len(name) + 1
    for i in range(0, -len(name), -1) :
        alphabet = ord(name[i])
        if alphabet != 65 :
            condition = 78
            if alphabet <= condition :
                for j in range(66, 91) :
                    total += 1
                    if alphabet == j :
                        break
            else :
                for j in range(90, 65, -1) :
                    total += 1
                    if alphabet == j :
                        break           
        value = True
        for tmp in [name[x] for x in range(i-1, -len(name), -1)] :
            if tmp != "A" :
                value = False
                break
        if value == True :
            break
        
        total += 1
    return total


def solution(name):
    # "A" = 65
    # "Z" = 90
    answer_foward = forward(name)
    answer_backward = backward(name)

    return min(answer_foward,answer_backward)

