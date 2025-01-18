"""
[Input]
1. info: List[int]
   - 각 노드의 동물 정보
   - 0: 양, 1: 늑대
   - 인덱스가 노드 번호

2. edges: List[List[int]]
   - 트리의 간선 정보
   - [부모, 자식] 형태
   - 루트는 항상 0번

[Output]
- result: int
  - 모을 수 있는 최대 양의 수
  - 늑대 수가 양 이하일 때만 이동 가능
"""

"""
[문제 특징] : [알고리즘 선택 이유]
1. 상태 기반 탐색 필요 : BFS로 상태 공간 탐색
2. 조건부 이동 존재 : 양/늑대 수 비교로 이동 제한
3. 방문 가능 노드 관리 : set으로 효율적 관리
4. 최적해 탐색 필요 : 모든 가능한 경로 탐색
5. 트리 구조 활용 : 인접 리스트로 구현
"""

"""
[자료구조]
1. tree: List[List[int]]
   - 인접 리스트로 구현된 트리
   - tree[i]: i번 노드의 자식들

2. queue: Deque[(node, sheep, wolf, available)]
   - node: 현재 노드
   - sheep: 현재 양 수
   - wolf: 현재 늑대 수
   - available: 방문 가능한 다음 노드들

[알고리즘: State Space BFS]
procedure find_max_sheep(info, edges):
    1. Initialize:
       - 트리 구조 구축
       - 시작 상태 큐에 삽입
    
    2. BFS:
       - 현재 상태에서 가능한 모든 다음 노드로
       - 양/늑대 수 조건 확인
       - 방문 가능 노드 집합 갱신
    
    3. Return 최대 양 수
"""

from collections import deque

def build_tree(info, edges):
    """인접 리스트로 트리 구축"""
    n = len(info)
    tree = [[] for _ in range(n)]
    for parent, child in edges:
        tree[parent].append(child)
    return tree

def solution(info, edges):
    tree = build_tree(info, edges)
    max_sheep = 0
    
    # (현재 노드, 양 수, 늑대 수, 방문 가능한 노드들)
    q = deque([(0, 1, 0, {child for child in tree[0]})])
    
    while q:
        node, sheep, wolves, available = q.popleft()
        max_sheep = max(max_sheep, sheep)
        
        # 방문 가능한 모든 노드에 대해
        for next_node in available:
            next_sheep = sheep + (not info[next_node])
            next_wolves = wolves + info[next_node]
            
            # 양이 늑대보다 많은 경우만 진행
            if next_sheep > next_wolves:
                # 다음 방문 가능한 노드 집합 계산
                next_available = available | set(tree[next_node]) - {next_node}
                q.append((next_node, next_sheep, next_wolves, next_available))
    
    return max_sheep

# 예시 실행
# info = [0,0,1,1,1,0,1,0,1,0,1,1]
# edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
# print(solution(info, edges))  # 5
