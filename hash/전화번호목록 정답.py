def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) - 1) :
        if phone_book[i+1].startswith(phone_book[i]) :
            answer = False
            break
        else :
            continue
    
    return answer


def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

#hash 정석으로 푼거
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer