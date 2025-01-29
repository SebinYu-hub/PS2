#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# 고유해야함
# [실생활 예시] : [알고리즘 본질]
# 1. 친구 목록 관리 : 중복 없는 친구 목록 유지
# 2. 방문 기록 체크 : 이미 방문한 웹사이트 관리
# 3. 투표 시스템 : 중복 투표 방지를 위한 투표자 관리

# [코딩테스트 꿀팁]
# 1. in 연산 효율
#    - list: O(n)
#    - set: O(1)
# 2. 집합 연산 활용
#    - union(): 합집합
#    - intersection(): 교집합
#    - difference(): 차집합
# 3. 중복 제거 시 활용
#    - list(set(items)): 중복 제거
#    - 순서가 중요하면 dict.fromkeys() 사용

# 집합 s 생성
s = set()

# s.add(item): 집합 s에 요소 item을 추가합니다.
# 반환값: 없음
# 시간 복잡도: O(1)
s.add(1)  # 현재 집합: {1}
print(s)  # 출력: {1}

# s.remove(item): 집합 s에서 요소 item을 제거합니다. item이 s에 없을 경우 KeyError를 발생시킵니다.
# 반환값: 없음
# 시간 복잡도: O(1)
s.remove(1)  # 현재 집합: {}
print(s)  # 출력: set()

# s.discard(item): 집합 s에서 요소 item을 제거합니다. item이 s에 없어도 에러가 발생하지 않습니다.
# 반환값: 없음
# 시간 복잡도: O(1)
s.discard(1)  # 현재 집합: {} (아무 변화 없음)
print(s)  # 출력: set()

# 집합 s와 s2 생성 및 초기화
s = {1, 2, 3}
s2 = {3, 4, 5}

# s.union(s2): 집합 s와 s2의 합집합을 반환합니다.
# 반환값: 합집합
# 시간 복잡도: O(len(s) + len(s2))
print(s.union(s2))  # 출력: {1, 2, 3, 4, 5}

# s.intersection(s2): 집합 s와 s2의 교집합을 반환합니다.
# 반환값: 교집합
# 시간 복잡도: O(min(len(s), len(s2)))
print(s.intersection(s2))  # 출력: {3}

# s.difference(s2): 집합 s에서 s2의 요소를 제거한 차집합을 반환합니다.
# 반환값: 차집합
# 시간 복잡도: O(len(s))
print(s.difference(s2))  # 출력: {1, 2}

# set(list): 리스트를 집합으로 변환합니다.
# 반환값: 집합
# 시간 복잡도: O(len(list))
print(set([6, 7, 8]))  # 출력: {8,6,7}, {6,7,8} 등 으로 나타남, 집합은 순서를 보장하지 않으므로 순서 달라질수 있음

# item in s: 집합 s에 item이 포함되어 있는지 확인합니다.
# 반환값: bool (True 또는 False)
# 시간 복잡도: O(1)
print(1 in s)  # 출력: True

# 실제 활용 예시 - 중복 방문 체크
visited = set()
paths = ['A', 'B', 'A', 'C', 'B', 'D']

for path in paths:
    if path in visited:
        print(f"{path}는 이미 방문했습니다.")
    else:
        visited.add(path)
        print(f"{path}를 처음 방문했습니다.")

# 출력:
# A를 처음 방문했습니다.
# B를 처음 방문했습니다.
# A는 이미 방문했습니다.
# C를 처음 방문했습니다.
# B는 이미 방문했습니다.
# D를 처음 방문했습니다.
