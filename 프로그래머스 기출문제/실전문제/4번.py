# 못풀었음
# "0111" 같이
# 01이 붙어 있거나 10이 붙어 있을 때 삭제하고 남은 길이를 리턴하는 문제인데
# del 하면서 새로 string을 만들어줘야 하는데 맥시멈 콜스택이 자꾸 나와서 애먹어서 못 풀음


def solution(string):
    count = 0

    def func(s):
        nonlocal count, string
        value = False
        for i in range(len(s) - 1):
            if (s[i] == "0" and s[i + 1] == "1") or (s[i] == "1" and s[i + 1] == "0"):
                string = s[:i] + s[i + 2 :]
                count += 1
                value = True
                break

        if value == True:
            func(s)
        else:
            return

    func(string)

    return len(string)


# def solution(s):
#     while True:
#         count = 0

#         for i in range(len(s) - 1):
#             if (s[i] == "0" and s[i + 1] == "1") or (s[i] == "1" and s[i + 1] == "0"):
#                 print(s)
#                 s = s[:i] + s[i + 2 :]
#                 print(s)
#                 count += 1
#                 break

#         if count == 0:
#             break

#     return count


print(solution("1011"))
