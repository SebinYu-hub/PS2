"""
[Input]
1. N: int
   - 전체 사람의 수
   - 제약: 1 ≤ N ≤ 1,000

2. K: int
   - 제거할 순서 간격
   - 제약: 1 ≤ K ≤ N

[Output]
- result: int
  - 마지막으로 남는 사람의 번호
  - 제약: 1 ≤ result ≤ N
  - 제약: 번호는 1부터 시작
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 원형 구조 필요 : deque의 rotate 활용
2. 순차적 제거 필요 : popleft 연산 활용
3. 효율적 회전 필요 : deque의 O(1) 회전
4. 순환 처리 필요 : rotate로 K번째 요소 접근
5. 메모리 효율성 필요 : deque 자료구조 활용
"""
"""
[자료구조]
1. queue: deque
   - 목적: 사람들의 순서 관리
   - 특징: 원형 큐처럼 동작
   - 연산: rotate(), popleft()

[알고리즘: Josephus Problem]
procedure solution(N, K):
    1. Initialize:
       - 1부터 N까지의 수를 deque에 저장
    
    2. Process elimination:
       - 큐 크기가 1이 될 때까지:
         a) K-1번 rotate하여 K번째 요소를 맨 앞으로
         b) popleft로 제거
    
    3. Return result:
       - 마지막 남은 요소 반환
"""

from collections import deque

def solution(N, K):
    # 1부터 N까지의 번호를 deque에 추가
    queue = deque(range(1, N+1))
    
    while len(queue) > 1:  # deque에 하나의 요소가 남을 때까지
        # K-1번 rotate하여 K번째 요소를 맨 앞으로 이동
        queue.rotate(-(K-1))
        queue.popleft()  # K번째 요소 제거
        
    return queue[0]  # 마지막으로 남은 요소 반환

# 예시 실행
# print(solution(7, 3))  # 3
# print(solution(5, 2))  # 3
