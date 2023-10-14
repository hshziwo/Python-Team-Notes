# 팁
# dfs 문제입니다.
# A, E, I, O, U 만을 사용하여 5자리 이내의 문자를 만들고, 정렬하여 주어지는 문자가 몇 번째인지 반환해야 합니다.
# 첫 번째 단어는 "A"이고, 두 번째 단어는 "AA"이며, 마지막 단어는 "UUUUU"입니다.
# 이 순서는 dfs(깊이 우선 탐색)을 통해 만들어지는 문자와 순서가 같습니다.
# 즉, dfs를 사용하여 문자를 만들고 만들어진 순서를 반환하면 됩니다.

def solution(word):
    words = ['A','E','I','O','U']
    max_length = 5

    elements = []

    def dfs(elements, text) :
        if len(text) > max_length :
            return
        
        if text not in elements :
            elements.append(text)

        for alphabet in words :
            dfs(elements, text + alphabet)

    for alphabet in words :
        dfs(elements, alphabet)

    answer = elements.index(word) + 1
    return answer