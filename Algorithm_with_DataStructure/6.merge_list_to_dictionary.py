#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 리스트를 딕셔너리로 병합하는 알고리즘은 두 개의 리스트를 키와 값 쌍으로 갖는 딕셔너리로 병합하는 알고리즘입니다.
# Python에서는 dict 함수와 zip 함수를 이용하여 두 리스트를 딕셔너리로 병합할 수 있습니다.
# 주의할 점은 두 리스트의 길이가 동일해야 합니다.

# [실생활 예시] : [알고리즘 본질]
# 1. 학생 정보 관리 : 학번 리스트와 이름 리스트를 학생 정보 사전으로 변환
# 2. 상품 가격표 생성 : 상품명 리스트와 가격 리스트를 가격표로 변환
# 3. 투표 결과 집계 : 후보자 리스트와 득표수 리스트를 결과로 변환

# [코딩테스트 꿀팁]
# 1. zip() 함수 활용
#    - zip()은 여러 이터러블을 병렬로 순회
#    - dict(zip(keys, values))로 간단히 변환
# 2. 딕셔너리 컴프리헨션
#    - {k:v for k,v in zip(keys,values)}
# 3. enumerate 활용
#    - dict(enumerate(values))로 인덱스를 키로 사용

def merge_list_to_dictionary(keys, values):
    return dict(zip(keys, values))

# 예시 사용법
keys = ["a", "b", "c"]
values = [1, 2, 3]
print(merge_list_to_dictionary(keys, values))  # 출력: {'a': 1, 'b': 2, 'c': 3}

# 실제 활용 예시 - 다양한 방법으로 딕셔너리 생성
# 1. 딕셔너리 컴프리헨션 사용
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
grade_dict = {name: score for name, score in zip(names, scores)}
print(grade_dict)  # 출력: {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# 2. enumerate 활용
items = ['apple', 'banana', 'orange']
indexed_dict = dict(enumerate(items))
print(indexed_dict)  # 출력: {0: 'apple', 1: 'banana', 2: 'orange'}
