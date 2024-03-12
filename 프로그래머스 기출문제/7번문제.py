# 배열이 주어질 때 각 수의 차가 같아지도록 하는 최소 swap의 횟수
# **2020 Dev-Matching 3번문제**
# https://lovelyalien.tistory.com/116
# https://jskim4.tistory.com/8
# [3번문제]
# 자연수 N개가 중복없이 들어있는 배열이 있을때  서로 다른 두 원소의 위치를 
# 바꾸는 Swap 연산을 이용해 원소들의 위치를 바꿔 서로 인접한 원소의 차가 K 이하가 
# 되도록 하는데 Swap 연산을 가장 적게 사용하였을때의 연산 횟수를 출력하는 문제였습니다.
# [3번 풀이]
# 자연수 배열의 최대길이가 8로 매우 작아 모든 순서쌍을 구한후 인접 크기의 차이가
# K이하인지를 검사하며 만약 K이하일 경우 입력배열에서 Swap을 몇번 사용해야지 해당
# 배열을 만들 수 있는지를 계산하여 풀었습니다.

# function solution7(k, numbers) {
#     let swapCount = 0;
#     let answer = Infinity;
#     const numberLength = numbers.length;

#     const permutation = (depth) => {
#         if (depth == numberLength) {
#             console.log(numbers);
#             let flag = true;
#             for(let i = 1 ; i < numberLength ; i++) {
#                 if ( k < Math.abs(numbers[i - 1] - numbers[i])) {
#                     flag = false;
#                     break;
#                 }
#             }
#             if (flag == true) {
#                 answer = Math.min(answer, swapCount);
#             }
#         }

#         for (let i = depth ; i < numberLength ; i++) {
#             if (i != depth) {
#                 swap(i, depth);
#                 swapCount++;
#             }

#             permutation(depth + 1);

#             if (i != depth) {
#                 swap(depth, i);
#                 swapCount--;
#             }
#         }
#     }

#     const swap = (ind1, ind2) => {
#         const temp = numbers[ind2];
#         numbers[ind2] = numbers[ind1];
#         numbers[ind1] = temp;
#     }

#     permutation(0);
#     console.log(answer);
# }

# const data = 3;
# const data2 = [3,7,2,8,6,4,5,1];
# /* const data = 10;
# const data2 = [10,30,40,20]; */

def solution7(k, numbers) :
    global swap_count, answer, numbers_length
    swap_count = 0
    answer = 9999999999
    numbers_length = len(numbers)

    def permutate(depth) :
        global swap_count, answer, numbers_length
        if depth == numbers_length :
            flag = True
            # 간격이 k보다 크면 False
            for i in range(1, numbers_length) :
                if abs(numbers[i - 1] - numbers[i]) > k :
                    flag = False
                    break

            if flag == True :
                print(numbers)
                answer = min(answer, swap_count)

        for i in range(depth, numbers_length) :
            # 자신 이외부터 스왑시작
            if i != depth :
                numbers[i], numbers[depth] = numbers[depth], numbers[i]
                swap_count += 1

            permutate(depth + 1)

            # 자신 이외부터 스왑 되돌림
            if i != depth :
                numbers[i], numbers[depth] = numbers[depth], numbers[i]
                swap_count -= 1

    permutate(0)
    print(answer)

solution7(20, [10,40,30,20])
# solution7(3, [3,7,2,8,6,4,5,1])
# solution7(10, [10,30,40,20])