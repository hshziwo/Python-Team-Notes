# 내가 푼거
def solution(nums):
    # set길이가 nums/2보다 크면 nums/2를 출력하고
    # 그냥 set으로 묶어버리고
    # set길이가 작거나 같으면 그냥 set길이를 출력
    set_array = set(nums)
    if len(set_array) > len(nums) / 2:
        return len(nums) / 2
    else:
        return len(set_array)


# 간결 문장
# 그냥 min으로 한방에 하네
def solution(ls):
    return min(len(ls) / 2, len(set(ls)))
