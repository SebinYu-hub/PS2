"""
[Input]
1. maps: List[List[int]]
   - N x M 크기의 2차원 배열
   - 0: 벽, 1: 길
   - (0,0)에서 시작
   - (N-1,M-1)이 도착점

[Output]
- result: int
  - 도착점까지의 최단 거리
  - 시작점과 도착점 포함해서 카운트
  - 도달 불가능: -1 반환
"""

"""
[문제 특징] : [알고리즘 선택 이유]
1. 최단 경로 탐색 필요 : BFS 알고리즘 선택
2. 격자 기반 이동 : 4방향 이동 벡터 활용
3. 거리 누적 필요 : 방문 배열에 거리 정보 저장
4. 도달 가능성 체크 : 방문 여부로 판단
5. 경계 처리 필요 : 유효한 좌표 검사
"""

"""
[자료구조]
1. dist: List[List[int]]
   - 각 위치까지의 최단 거리 저장
   - -1: 미방문, 양수: 거리

2. queue: Deque[Tuple[int, int]]
   - BFS를 위한 좌표 큐
   - (row, col) 형태로 저장

[알고리즘: Grid BFS]
procedure find_shortest_path(maps):
    1. Initialize:
       - 거리 배열 초기화
       - 시작점 큐에 추가
    
    2. BFS:
       - 4방향 탐색
       - 유효한 이동만 처리
       - 거리 정보 갱신
    
    3. Return 도착점 거리 or -1
"""


from collections import deque

def solution(maps):
    # 최적화 1: 방향 벡터를 튜플로 선언하여 불변성 보장
    MOVES = ((-1, 0), (0, -1), (0, 1), (1, 0))  # 상, 좌, 우, 하
    
    # 최적화 2: 맵 크기를 상수로 저장하여 반복적 접근 최소화
    N, M = len(maps), len(maps[0])
    
    # 최적화 3: list comprehension으로 거리 배열 초기화
    # @reference/list_comprehension.py 참조
    dist = [[-1] * M for _ in range(N)]
    dist[0][0] = 1  # 시작 위치 거리 초기화
    
    # 최적화 4: deque 사용으로 큐 연산 최적화
    # @performance/list_vs_deque_pop_performance.py 참조
    queue = deque([(0, 0)])  # (row, col) 형태로 저장
    
    while queue:
        row, col = queue.popleft()
        
        # 최적화 5: 방향 이동을 튜플 언패킹으로 처리
        for dx, dy in MOVES:
            next_row, next_col = row + dx, col + dy
            
            # 최적화 6: 범위 체크와 방문/벽 체크를 한번에 처리
            # @mistake/indexing_convention_tutorial.py 참조
            if (0 <= next_row < N and 0 <= next_col < M and 
                maps[next_row][next_col] == 1 and dist[next_row][next_col] == -1):
                dist[next_row][next_col] = dist[row][col] + 1
                queue.append((next_row, next_col))
    
    return dist[N-1][M-1]  # 도착점의 거리 반환

# 예시 실행
# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
