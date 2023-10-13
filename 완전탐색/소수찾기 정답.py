from itertools import permutations
def solution(numbers):
    count = 0
    test_number = []

    for i in range(len(numbers)):
        case = list(set(map(''.join,permutations(numbers,i+1))))
        for j, number in enumerate(case):
            test_number.append(int(number))

    test_number = list(set(test_number))
    for i, number in enumerate(test_number):
        if isPrime(number)== True:
            count +=1

    return count



def isPrime(x):
    if x<2:
        return False
    else:
        for i in range(2,x):
            if x % i == 0:
                return False

    return True