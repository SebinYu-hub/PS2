"""
[Input]
1. n: int
   - 송전탑 개수
   - 2 ≤ n ≤ 100

2. wires: List[List[int]]
   - 전선 정보 [v1, v2]
   - v1, v2: 연결된 송전탑 번호
   - 전선 개수는 n-1개

[Output]
- result: int
  - 두 전력망의 송전탑 개수 차이의 최솟값
"""

"""
[문제 특징] : [알고리즘 선택 이유]
1. 트리 구조 분석 필요 : 인접 리스트로 그래프 표현
2. 간선 제거 효과 분석 : DFS로 서브트리 크기 계산
3. 모든 간선 시도 필요 : 완전 탐색으로 최적해 도출
4. 연결 요소 크기 계산 : DFS로 연결된 노드 수 계산
5. 최소 차이 갱신 필요 : 그리디하게 최소값 갱신
"""

"""
[자료구조]
1. graph: List[List[int]]
   - 인접 리스트로 구현된 트리
   - graph[i]: i번 노드와 연결된 노드들

[알고리즘: Edge Removal & DFS]
procedure find_minimum_difference(n, wires):
    1. Initialize:
       - 그래프 구성
       - 최소 차이값 초기화
    
    2. For each wire:
       - 간선 제거
       - DFS로 분리된 두 부분의 크기 계산
       - 차이 최소값 갱신
       - 간선 복구
    
    3. Return 최소 차이값
"""
from decorators import solution_logger

@solution_logger()
def solution(n, wires):
    # 최적화 1: list comprehension으로 그래프 초기화
    # @reference/list_comprehension.py 참조
    graph = [[] for _ in range(n + 1)]
    
    # 최적화 2: 양방향 그래프 구성을 한번에 처리
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    # 최적화 3: DFS 함수를 내부에 정의하여 변수 접근 최적화
    # @mistake/variable_scope_tutorial.py 참조
    def dfs(node, parent):
        count = 1  # 현재 노드 포함
        # 최적화 4: 자식 노드들의 서브트리 크기 합산
        for child in graph[node]:
            if child != parent:  # 부모 노드가 아닌 경우만 탐색
                count += dfs(child, node)
        return count
    
    min_diff = float("inf")
    
    # 최적화 5: 간선을 하나씩 제거하고 DFS로 크기 차이 계산
    for a, b in wires:
        # 최적화 6: 간선 제거
        graph[a].remove(b)
        graph[b].remove(a)
        
        # 최적화 7: 두 서브트리의 크기 차이 계산
        count_a = dfs(a, b)
        count_b = n - count_a
        
        # 최적화 8: 최소 차이 갱신
        min_diff = min(min_diff, abs(count_a - count_b))
        
        # 최적화 9: 간선 복구
        graph[a].append(b)
        graph[b].append(a)
    
    return min_diff

# 예시 실행
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))  # 3
print(solution(4, [[1,2],[2,3],[3,4]]))  # 0
