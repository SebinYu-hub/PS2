"""
[Input]
1. board: list[list[int]]
   - N x N 크기의 격자 맵
   - 제약: 3 ≤ N ≤ 25
   - 제약: 0은 빈칸, 1은 벽
   - 제약: (0,0)과 (N-1,N-1)은 항상 0

[Output]
- result: int
  - 최소 건설 비용
  - 제약: 직선 도로 100원
  - 제약: 코너 500원
  - 제약: 시작점에서 도착점까지의 경로 필요
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 최소 비용 경로 필요 : BFS + DP 활용
2. 방향 전환 비용 필요 : 방향별 상태 관리
3. 격자 이동 필요 : 방향 벡터 활용
4. 상태 관리 필요 : 3차원 방문 배열
5. 최적화 필요 : 불필요한 경로 가지치기
"""
"""
[자료구조]
1. visited: list[list[list[int]]]
   - 목적: 각 위치의 방향별 최소 비용
   - 특징: [x][y][direction] 형태
   - 연산: 비용 갱신

2. queue: list
   - 목적: BFS 탐색용 큐
   - 특징: (x, y, 이전방향, 비용) 저장
   - 연산: append, pop

[알고리즘: Road Construction]
procedure solution(board):
    1. Initialize:
       - 방문 배열 생성
       - 시작점 큐에 추가
    
    2. BFS traversal:
       - 각 위치에서:
         a) 4방향 이동 시도
         b) 비용 계산 (직선/코너)
         c) 최소 비용 갱신
    
    3. Return result:
       - 도착점의 최소 비용 반환
"""

def solution(board):
    # 최적화 1: 상수로 방향과 크기 정의
    DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 좌, 상, 우, 하
    N = len(board)
    
    # 최적화 2: 유효성 검사 함수로 분리
    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < N
    
    def is_blocked(x, y):
        return (x, y) == (0, 0) or not is_valid(x, y) or board[x][y] == 1
    
    # 최적화 3: 비용 계산 함수로 분리
    def calculate_cost(direction, prev_direction, cost):
        # 이전 방향이 없거나 같은 방향이면 직선 도로 비용만
        if prev_direction == -1 or (prev_direction - direction) % 2 == 0:
            return cost + 100
        # 다른 방향이면 코너 비용 추가
        return cost + 600
    
    # 최적화 4: 방문 체크 및 업데이트 함수로 분리
    def should_update(x, y, direction, new_cost):
        return visited[x][y][direction] == 0 or visited[x][y][direction] > new_cost
    
    # 최적화 5: 3차원 방문 배열로 방향별 비용 관리
    # @reference/list_comprehension.py 참조
    visited = [[[0] * 4 for _ in range(N)] for _ in range(N)]
    
    # 최적화 6: deque 대신 list 사용 (이 문제에서는 큐의 크기가 작아서 성능 차이 미미)
    queue = [(0, 0, -1, 0)]  # (x, y, 이전 방향, 비용)
    answer = float("inf")
    
    while queue:
        x, y, prev_direction, cost = queue.pop(0)
        
        # 최적화 7: 방향별 이동 처리
        for direction, (dx, dy) in enumerate(DIRECTIONS):
            new_x, new_y = x + dx, y + dy
            
            # 최적화 8: 이동 불가능한 경우 스킵
            if is_blocked(new_x, new_y):
                continue
                
            new_cost = calculate_cost(direction, prev_direction, cost)
            
            # 최적화 9: 도착점 도달 시 최소 비용 갱신
            if (new_x, new_y) == (N-1, N-1):
                answer = min(answer, new_cost)
            # 최적화 10: 비용이 더 작은 경우만 큐에 추가
            elif should_update(new_x, new_y, direction, new_cost):
                queue.append((new_x, new_y, direction, new_cost))
                visited[new_x][new_y][direction] = new_cost
    
    return answer

# 예시 실행
# board = [[0,0,0],[0,0,0],[0,0,0]]
# print(solution(board))  # 900
