def solution(number, k) :
    stack = []
    for n in number :
        while stack and k > 0 and stack[-1] < n :
            stack.pop()
            k -= 1

        stack.append(n)
    return ''.join(stack[:len(number) - k])


def solution(number, k):
    answer = ''
    idx = 0
    while True :
        max_num = ''
        for i in range(idx, k+1) :
            if int(number[i]) == 9 :
                max_num = number[i]
                idx = i + 1
                break
            if number[i] > max_num :
                max_num = number[i]
                idx = i + 1
        k += 1
        answer += max_num
        if k == len(number) :
            break       
    return answer