# 프로그래머스 | 폰켓몬
def solution(nums):
   
    #중복 제거한 폰켓몬 종류의 수
    poncatmon_kind_num = len(set(nums))
   
    #고를 수 있는 폰켓몬 수
    catch_num = len(nums) // 2
   
    #(폰켓몬 종류의 수)와 (고를 수 있는 수) 중에 교집합 하는 수가 답이므로 둘 중 작은 게 답
    result = min(poncatmon_kind_num, catch_num)
   
    return result