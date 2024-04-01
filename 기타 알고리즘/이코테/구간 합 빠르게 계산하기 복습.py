# 접두사 합(Prefix Sum)을 이용함.
# 즉, 0인덱스에는 0의 값을 가지고 n + 1 길이만큼의 array를 선언하고
# 1부터 길이까지의 구간합을 미리 구해놓는다.
# left = 2 right = 5 까지 구해라고 하면
# 실제 2자리부터 5자리까지 구해라이므로
# 이를 구간합 테이블로 보면
# 0인덱스에는 0값이고
# 구간합[5] - 구간합[2 - 1] 의 값
# 즉, 5까지의 구간합 - 1까지의 구간합을 구하면 2 ~ 5 자리까지의 구간합이 구해짐.
# 여기서 0인덱스의 값에 0을 넣은 이유는 실제 정수와 맞추기 위함도 있지만
# 2까지의 구간합을 구한다고 했을 때 공식상 구간합[2] - 구간합[1 - 1] 이 성립하기 위함임.

n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]
for i in data:
    # 누적합을 계속 prefix_sum에 append함
    sum_value += i
    prefix_sum.append(sum_value)

left = 3
right = 4
# prefix_sum[right] - prefix_sum[left - 1] 이거 자체가 left ~ right 까지의 구간합 공식임
print(prefix_sum[right] - prefix_sum[left - 1])
