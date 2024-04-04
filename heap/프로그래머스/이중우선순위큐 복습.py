def solution(operations):
    # deque으로 풀고 싶었으나
    # 그냥 list로 하는 게 더 쉬움
    array = []
    for oper in operations:
        if "I " in oper:
            array.append(int(oper.split(" ")[1]))
            array.sort()
        else:
            if len(array) < 1:
                continue

            if "D 1" == oper:
                array.pop()
            elif "D -1" == oper:
                array.pop(0)

    if array:
        return [array[-1], array[0]]
    else:
        return [0, 0]
