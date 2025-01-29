#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 중복 원소 제거 알고리즘은 리스트에서 중복되는 원소를 제거하는 알고리즘입니다.
# Python에서는 set 자료형을 이용하여 쉽게 중복을 제거할 수 있으며,
# 이를 다시 list로 변환하여 중복이 제거된 리스트를 얻을 수 있습니다.

# [실생활 예시] : [알고리즘 본질]
# 1. 이메일 수신자 목록 : 중복된 이메일 주소 제거
# 2. 방문 기록 정리 : 중복 방문 기록 제거
# 3. 장바구니 상품 목록 : 중복된 상품 ID 제거

# [코딩테스트 꿀팁]
# 1. set vs dict.fromkeys
#    - set: 순서 무관할 때
#    - dict.fromkeys: 순서 유지 필요할 때
# 2. 리스트 컴프리헨션 활용
#    - seen = set()
#    - [x for x in arr if not (x in seen or seen.add(x))]
# 3. pandas unique
#    - 대용량 데이터는 pd.unique() 고려

def remove_duplicates(arr):
    return list(set(arr))

# 예시 사용법
arr = [1, 2, 2, 3, 3, 4]
print(remove_duplicates(arr))  # 출력: [1, 2, 3, 4] (순서는 변할 수 있음)

# 실제 활용 예시 - 다양한 중복 제거 방법
# 1. 순서 유지하면서 중복 제거
def remove_duplicates_ordered(arr):
    return list(dict.fromkeys(arr))

# 2. 리스트 컴프리헨션으로 중복 제거
def remove_duplicates_with_seen(arr):
    seen = set()
    return [x for x in arr if not (x in seen or seen.add(x))]

# 테스트
numbers = [1, 3, 2, 3, 1, 4, 2]
print(remove_duplicates_ordered(numbers))       # 출력: [1, 3, 2, 4]
print(remove_duplicates_with_seen(numbers))     # 출력: [1, 3, 2, 4]

# 문자열 리스트에서도 동작
words = ['apple', 'banana', 'apple', 'cherry', 'banana']
print(remove_duplicates_ordered(words))         # 출력: ['apple', 'banana', 'cherry']
