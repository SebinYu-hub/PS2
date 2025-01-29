#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# [실생활 예시] : [알고리즘 본질]
# 1. 프린터 인쇄 대기열 : 순서대로 처리되는 인쇄 작업
# 2. 티켓 예매 대기열 : 선착순으로 처리되는 예매 요청
# 3. 은행 창구 대기열 : 먼저 온 고객부터 서비스 제공

# [코딩테스트 꿀팁]
# 1. deque vs list
#    - deque: O(1)로 양쪽 끝 접근
#    - list: pop(0)이 O(n), 비효율적
# 2. BFS에서 필수
#    - 그래프/트리 레벨 단위 탐색
#    - 최단 경로 찾기
# 3. maxlen 활용
#    - 최근 N개 이력 관리
#    - 슬라이딩 윈도우 구현

from collections import deque

# 큐 객체 초기화
queue = deque()

# 요소들을 큐에 삽입 (enqueue)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

# 큐에서 요소들을 제거 (dequeue)하면서 출력
while queue:
    print(queue.popleft())  # 출력: 1, 2, 3, 4, 5 (FIFO 순서)

# 실제 활용 예시 - 최근 작업 이력 관리
recent_tasks = deque(maxlen=3)  # 최근 3개만 유지
tasks = ['작업1', '작업2', '작업3', '작업4', '작업5']

for task in tasks:
    recent_tasks.append(task)
    print(f"현재 최근 작업: {list(recent_tasks)}")

# 출력:
# 현재 최근 작업: ['작업1']
# 현재 최근 작업: ['작업1', '작업2']
# 현재 최근 작업: ['작업1', '작업2', '작업3']
# 현재 최근 작업: ['작업2', '작업3', '작업4']
# 현재 최근 작업: ['작업3', '작업4', '작업5']

