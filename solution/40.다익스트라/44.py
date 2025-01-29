"""
[Input]
1. N: int
   - 마을의 개수
   - 1 ≤ N ≤ 50

2. road: List[List[int]]
   - [마을1, 마을2, 시간] 형태의 도로 정보
   - 양방향 도로
   - 시간: 배달 소요 시간

3. K: int
   - 배달 가능한 최대 시간

[Output]
- result: int
  - K시간 이내에 배달 가능한 마을의 개수
  - 1번 마을에서 출발
"""

"""
[문제 특징] : [알고리즘 선택 이유]
1. 최단 거리 계산 필요 : 다익스트라 알고리즘 선택
2. 가중치 있는 그래프 : 우선순위 큐로 최적화
3. 시간 제한 존재 : K 이하인 경우만 카운트
4. 양방향 도로 : 무방향 그래프로 구현
5. 1번 마을 기준 : 단일 출발점 최단 경로
"""

"""
[자료구조]
1. graph: List[List[Tuple[int, int]]]
   - 인접 리스트로 구현된 그래프
   - (도착마을, 소요시간) 형태의 튜플 저장

2. distances: List[int]
   - 각 마을까지의 최단 시간 저장
   - float('inf')로 초기화

[알고리즘: Dijkstra's Shortest Path]
procedure count_reachable_towns(N, road, K):
    1. Initialize:
       - 그래프 구성
       - 거리 배열 초기화
       - 우선순위 큐 생성
    
    2. Dijkstra:
       - 현재까지의 최단 시간 갱신
       - 더 긴 경로는 스킵
       - 모든 인접 마을 검사
    
    3. Return K 이하 시간인 마을 수
"""

import heapq

def solution(N, road, K):
    # 최적화 1: list comprehension으로 그래프와 거리 배열 초기화
    # @reference/list_comprehension.py 참조
    graph = [[] for _ in range(N + 1)]
    distances = [float("inf")] * (N + 1)
    distances[1] = 0  # 시작점 거리 초기화
    
    # 최적화 2: 양방향 그래프 구성을 한번에 처리
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    
    # 최적화 3: 힙을 사용하여 최단 거리 노드 선택
    # @performance/list_vs_heapq.py 참조
    heap = [(0, 1)]  # (거리, 노드) 형태로 저장
    
    while heap:
        # heapq.heappop = 문법
        dist, node = heapq.heappop(heap) # 거리 기준 정렬
        
        # 최적화 4: 현재 거리가 이미 저장된 거리보다 큰 경우 스킵
        if dist > distances[node]:
            continue
            
        # 최적화 5: 인접 노드 탐색 및 거리 갱신
        for next_node, next_dist in graph[node]:
            cost = dist + next_dist
            if cost < distances[next_node]:
                distances[next_node] = cost
                heapq.heappush(heap, (cost, next_node))
    
    # 최적화 6: list comprehension으로 결과 계산
    return sum(1 for dist in distances if dist <= K)

# 예시 실행
# print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))  # 4
# print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))  # 4
