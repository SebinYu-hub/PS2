#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# [실생활 예시] : [알고리즘 본질]
# 1. 전화번호부 : 이름(key)으로 전화번호(value) 빠르게 찾기
# 2. 학생 성적 관리 : 학번(key)으로 성적 정보(value) 관리
# 3. 장바구니 상품 수량 : 상품ID(key)로 수량(value) 관리

# [코딩테스트 꿀팁]
# 1. 해시맵 구현 문제에서 필수
# 2. Counter 클래스 활용 (from collections import Counter)
#    - 리스트 요소 개수 세기: Counter(['a','a','b']) -> {'a':2, 'b':1}
# 3. defaultdict 활용 (from collections import defaultdict)
#    - 키 없을 때 기본값 자동 생성

# dic.get(key)
# 딕셔너리 dic에서 주어진 key에 해당하는 값을 반환합니다. 
# key가 딕셔너리에 없으면 None을 반환합니다.
# 시간 복잡도: O(1)
dic = {'a': 1, 'b': 2, 'c': 3}
value = dic.get('a')
print(value)  # 출력값: 1
value = dic.get('d')
print(value)  # 출력값: None

# dic[key]
# 딕셔너리 dic에서 주어진 key에 해당하는 값을 반환합니다. 
# key가 딕셔너리에 없으면 KeyError를 발생시킵니다.
# 시간 복잡도: O(1)
try:
    value = dic['b']
    print(value)  # 출력값: 2
    value = dic['d']
    print(value)  # 출력값: (이 줄은 실행되지 않습니다; KeyError 발생)
except KeyError as e:
    print(e)  # 출력값: 'd'

# dic.pop(key)
# 딕셔너리 dic에서 주어진 key에 해당하는 항목을 제거하고 그 값을 반환합니다. 
# key가 딕셔너리에 없으면 KeyError를 발생시킵니다.
# 시간 복잡도: O(1)
try:
    value = dic.pop('c')
    print(value)  # 출력값: 3
    value = dic.pop('d')
    print(value)  # 출력값: (이 줄은 실행되지 않습니다; KeyError 발생)
except KeyError as e:
    print(e)  # 출력값: 'd'

# key in dic
# 주어진 key가 딕셔너리 dic에 있는지를 검사합니다. 
# 시간 복잡도: O(1)
key_presence = 'a' in dic
print(key_presence)  # 출력값: True
key_presence = 'd' in dic
print(key_presence)  # 출력값: False

# 실제 활용 예시 - 문자열 내 문자 개수 세기
from collections import Counter
text = "hello world"
char_count = Counter(text)
print(char_count)  # 출력: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
