# 무작위 숫자가 들어간 배열에 숫자가 1부터 순차적으로 모두 들어가 있는지
# function solution1(numArr) {
#     const maxNum = Math.max(...numArr);
#     const length = numArr.length;
#     let answer = false;
#     if (maxNum == length) {
#         answer = true;
#     }
#     console.log(answer);
# }

# const solution1Data = [1, 4, 3, 2, 5];

# 정렬 후 순차적으로 되어 있다면 마지막 값과 length가 동일
def solution1(numArr) :
    answer = False
    if len(numArr) == max(numArr) :
        answer = True

    return answer

value = [1,4,3,2,5]
print(solution1(value))

