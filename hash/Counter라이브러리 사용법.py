from collections import Counter

counter = Counter(["red", "blue", "red", "green", "blue", "blue"])

print(counter["blue"])  # blue의 카운터수 출력
print(counter["green"])  # green의 카운터수 출력
dict_x = dict(counter)  # Counter 객체를 dict 자료형으로 변환시킴
print(dict_x)  # {'red': 2, 'blue': 3, 'green': 1}

# 출력값
# 3
# 1
# {'red': 2, 'blue': 3, 'green': 1}


# 카운터(Counter) 사용법
# from collections import Counter
# counter = Counter(['a', 'a', 'b', 'c', 'c'])
# counter['a'] -> 2 #카운터 객체에 값에 해당하는 게 몇 개 있는 지 수를 세줌
# counter['b'] -> 1
# dict(counter) -> {'a': 2. 'b': 1, 'c':2} #dict로 변환하면 사전형태로 정보를 변환해줌
# dict같이 편하게 변환할 수 있기 때문에 Counter라이브러리 써서
# 워드클라우드 같은 기능을 만들 때 유용하게 사용할 수 있음
# 카운터 객체는 set처럼 빼기가 가능하다
# 따라서 차집합 문제에 오히려 set보다 편하게 적용 가능 set은 중복을 제거해버려서 문제
# 완주하지못한선수 복습.py 파일으로 확인할 것
