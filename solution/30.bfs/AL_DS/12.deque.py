#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# [실생활 예시] : [알고리즘 본질]
# 1. 은행 창구 대기열 : 양쪽에서 고객 입/출입이 가능한 대기열 관리
# 2. 웹 브라우저 방문 기록 : 앞으로/뒤로 가기 기능 구현
# 3. 포토샵 실행취소(undo)/재실행(redo) : 양방향 작업 이력 관리

# [코딩테스트 꿀팁]
# 1. list vs deque
#    - list: pop(0)는 O(n), append/pop()은 O(1)
#    - deque: 양쪽 모두 O(1)
# 2. BFS 구현시 deque 필수 (성능차이 큼)
# 3. maxlen 파라미터로 최대 크기 제한 가능

from collections import deque

# 데크 객체 생성
deq = deque()

# append(item): 데크의 오른쪽 끝에 item을 추가합니다.
# 반환값: 없음
# 시간 복잡도: O(1)
deq.append(1)  # 현재 데크: deque([1])
print(deq)  # 출력: deque([1])

# appendleft(item): 데크의 왼쪽 끝에 item을 추가합니다.
# 반환값: 없음
# 시간 복잡도: O(1)
deq.appendleft(0)  # 현재 데크: deque([0, 1])
print(deq)  # 출력: deque([0, 1])

# popleft(): 데크의 왼쪽 끝 요소를 제거하고 그 요소를 반환합니다.
# 반환값: 제거된 요소
# 시간 복잡도: O(1)
deq.popleft()  # 현재 데크: deque([1])
print(deq)  # 출력: deque([1])

# deq[K]: 데크의 K번째 요소를 반환합니다.
# 반환값: K번째 요소
# 시간 복잡도: O(1)
print(deq[0])  # 출력: 1

# 실제 활용 예시 - 슬라이딩 윈도우
window = deque(maxlen=3)
for i in range(5):
    window.append(i)
    print(list(window))  # 3개씩 묶어서 출력
