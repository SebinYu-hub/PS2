from heapq import heappush, heappop

def solution(land, height):
    """
    [Input]
    1. land: List[List[int]]
       - N x N 격자의 높이 정보
       - 제약: N > 0

    2. height: int
       - 사다리 없이 이동 가능한 높이 차이
       - 제약: height > 0

    [Output]
    - result: int
      - 모든 칸을 연결하는데 필요한 최소 비용
      - 제약: result >= 0
    """
    """
    [문제 특징] : [알고리즘 선택 이유]
    1. "최소 비용" 경로 찾기 필요 : 우선순위 큐 기반 알고리즘
    2. 격자 형태의 그래프 탐색 : BFS/방향벡터 활용
    3. 비용이 다른 두 종류의 이동 : 다익스트라 변형 
    4. 모든 칸 연결 필요 : 완전탐색 보장
    5. 높이차에 따른 조건부 비용 : 가중치 그래프
    """
    """
    [자료구조]
    - PriorityQueue: (cost, row, col)
      - 목적: 최소 비용 경로 관리
      - 특징: O(log N) 삽입/삭제
    - visited: Boolean[][]
      - 목적: 방문 상태 추적
      - 특징: O(1) 접근

    [알고리즘: Modified Dijkstra's]
    procedure find_min_cost(land, height):
        1. Initialize:
           - PQ <- (0, start_pos)
           - visited[][] <- false
           
        2. While PQ not empty:
           - cost, pos <- PQ.pop()
           - if visited[pos]: continue
           - mark visited[pos]
           - add cost to total
           
           for each neighbor:
             if valid_pos && !visited:
               cost = height_diff > limit ? height_diff : 0
               PQ.push((cost, neighbor))

        3. Return total_cost
    """

    # 최적화 1: 상수로 방향과 크기 정의
    N = len(land)
    DR = [-1, 0, 1, 0]  # 상우하좌
    DC = [0, 1, 0, -1]
    
    # 최적화 2: 방문 배열을 list comprehension으로 초기화
    # @reference/list_comprehension.py 참조
    visited = [[False] * N for _ in range(N)]
    
    # 최적화 3: 우선순위 큐로 최소 비용 관리
    # @performance/list_vs_heapq.py 참조
    pq = [(0, 0, 0)]  # (비용, 행, 열)
    total_cost = 0
    
    # 최적화 4: BFS + 우선순위 큐로 최소 비용 경로 탐색
    while pq:
        cost, row, col = heappop(pq)
        
        # 최적화 5: 이미 방문한 위치는 스킵
        if visited[row][col]:
            continue
            
        visited[row][col] = True
        total_cost += cost
        
        # 최적화 6: 인접 위치 탐색
        for i in range(4):
            nrow, ncol = row + DR[i], col + DC[i]
            
            # 최적화 7: 유효한 위치만 처리
            if 0 <= nrow < N and 0 <= ncol < N and not visited[nrow][ncol]:
                # 최적화 8: 높이 차이에 따른 비용 계산
                diff = abs(land[row][col] - land[nrow][ncol])
                new_cost = diff if diff > height else 0
                heappush(pq, (new_cost, nrow, ncol))
    
    return total_cost

# 예시 실행
# print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))  # 15
# print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))  # 18
