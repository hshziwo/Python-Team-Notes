# def solution(numbers):
#     tmp = list(map(str, numbers))
#     tmp.sort(reverse=True)
#     answer = ''.join(tmp)
#     return answer


import functools

def solution(numbers):
    def comparator(a, b) :
        if int(a+b) > int(b+a) :
            return 1
        elif int(a+b) < int(b+a) :
            return -1
        else :
            return 0
        
    tmp = list(map(str, numbers))
    tmp.sort(reverse=True, key = functools.cmp_to_key(comparator))
    answer = ''.join(tmp)
    if tmp[0] == "0" :
        return "0"
    return answer