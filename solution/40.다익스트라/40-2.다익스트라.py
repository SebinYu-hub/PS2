"""
[Input]
1. graph: dict[str, dict[str, int]]
   - 그래프의 인접 리스트 표현
   - 제약: 1 ≤ len(graph) ≤ 100
   - 제약: 각 간선의 가중치는 양의 정수

2. start: str
   - 시작 노드
   - 제약: start는 graph의 키 중 하나

[Output]
- result: list[Any]
  - [distances, paths] 형태의 리스트
  - distances: 각 노드까지의 최단 거리
  - paths: 각 노드까지의 최단 경로
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 최단 경로 필요 : 다익스트라 알고리즘 활용
2. 경로 추적 필요 : 이전 노드 기록
3. 효율적 선택 필요 : 우선순위 큐 활용
4. 메모리 효율성 필요 : defaultdict 사용
5. 정렬 필요 : 결과의 정렬된 출력
"""
"""
[자료구조]
1. distances: defaultdict
   - 목적: 최단 거리 저장
   - 특징: 무한대로 초기화
   - 연산: 거리 갱신

2. queue: list
   - 목적: 우선순위 큐로 사용
   - 특징: (거리, 노드) 튜플 저장
   - 연산: heappush, heappop

[알고리즘: Dijkstra]
procedure solution(graph, start):
    1. Initialize:
       - 거리 배열과 경로 배열 초기화
       - 시작점 설정
    
    2. Process nodes:
       - 우선순위 큐로 노드 선택
       - 인접 노드의 거리 갱신
       - 경로 정보 업데이트
    
    3. Return result:
       - 최단 거리와 경로 반환
"""

import heapq
from collections import defaultdict

def solution(graph, start):
    # defaultdict 사용 - 무한대 초기화 O(1), KeyError 방지
    distances = defaultdict(lambda: float("inf"))
    distances[start] = 0
    
    # 우선순위 큐와 방문 체크 set 초기화
    queue = [(0, start)]  # (거리, 노드) 튜플로 구성
    visited = set()  # 방문 체크를 위한 set - O(1) 시간복잡도
    
    # defaultdict 사용 - 경로 저장 초기화 및 KeyError 방지
    paths = defaultdict(list)
    paths[start] = [start]

    while queue:
        # heappop 사용 - 최소 거리 노드 선택 O(logV)
        current_distance, current_node = heapq.heappop(queue)
        
        # 최적화: visited set으로 방문 체크 O(1)
        if current_node in visited:
            continue
        visited.add(current_node)

        # 인접 노드 탐색 - O(E)
        for adjacent_node, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # 최적화: 더 짧은 경로를 찾은 경우에만 갱신
            if distance < distances[adjacent_node]:
                distances[adjacent_node] = distance
                # list slicing으로 새로운 경로 생성
                paths[adjacent_node] = paths[current_node][:] + [adjacent_node]
                # heappush 사용 - 우선순위 큐 갱신 O(logV)
                heapq.heappush(queue, [distance, adjacent_node])

    # dict comprehension 사용 - 경로 정렬 O(VlogV)
    sorted_paths = {node: paths[node] for node in sorted(paths)}
    return [distances, sorted_paths]

# TEST 코드
# print(solution({ 'A': {'B': 9, 'C': 3}, 'B': {'A': 5}, 'C': {'B': 1} }, 'A'))
# print(solution({'A': {'B': 1}, 'B': {'C': 5}, 'C': {'D': 1}, 'D': {}}, 'A'))