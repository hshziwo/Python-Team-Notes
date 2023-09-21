def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)) :
        for j in range(i+1, len(phone_book)) :
            if phone_book[j].startswith(phone_book[i]) :
                answer = False
                break
        if answer == False :
            break
    
    return answer

# https://copro505.tistory.com/entry/%EC%A0%84%ED%99%94%EB%B2%88%ED%98%B8-%EB%AA%A9%EB%A1%9D 참고