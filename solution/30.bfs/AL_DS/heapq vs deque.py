
"""
heapq vs deque 비교
선택 기준
- deque: 순서대로 데이터를 처리하거나 양끝에서의 작업이 필요할 때
- heapq: 우선순위에 따라 데이터를 처리하거나 최소/최대값을 자주 찾아야 할 때

1. deque (Double-ended queue)
- 주요 특징: 양쪽 끝에서 빠른 삽입/삭제
- 시간복잡도: 양끝 삽입/삭제 O(1)
- 사용 케이스:
  - 슬라이딩 윈도우
  - BFS
  - 최근 이력 관리
  - 큐/스택 구현

"""
from collections import deque
import heapq

# deque - 슬라이딩 윈도우 예시
def deque_example():
    d = deque([1, 2, 3])
    d.append(4)      # 오른쪽 추가: [1, 2, 3, 4]
    d.appendleft(0)  # 왼쪽 추가: [0, 1, 2, 3, 4]
    d.pop()          # 오른쪽 제거: [0, 1, 2, 3]
    d.popleft()      # 왼쪽 제거: [1, 2, 3]
    return d
"""  
2. heapq (Priority Queue)  
- 주요 특징: 최소/최대값 빠른 접근과 자동 정렬
- 시간복잡도:
  - 삽입/삭제 O(log n)
  - 최소값 접근 O(1)
- 사용 케이스:
  - 우선순위 큐
  - K번째 큰/작은 수
  - 다익스트라 알고리즘
"""
# heapq 예시
def heapq_example():
    h = []
    heapq.heappush(h, 5)
    heapq.heappush(h, 3)
    heapq.heappush(h, 7)
    first = heapq.heappop(h)   # 3 (항상 최소값)
    second = heapq.heappop(h)  # 5
    return first, second