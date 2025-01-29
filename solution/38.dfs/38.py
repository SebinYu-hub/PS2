"""
[Input]
1. graph: List[List[str]]
   - 무방향 그래프의 간선 정보
   - [["노드1", "노드2"], ["노드2", "노드3"], ...]
   - 문자열로 표현된 노드들의 연결 관계

2. start: str
   - 탐색을 시작할 노드
   - 문자열로 표현된 시작점

[Output]
- result: List[str]
  - DFS 순회 결과를 담은 노드 리스트
  - 깊이 우선 탐색 순서대로 방문한 노드들
"""

"""
[문제 특징] : [알고리즘 선택 이유]
1. 그래프 순회 필요 : 반복적 DFS 알고리즘 선택
2. 무방향 그래프 : 양방향 연결 처리
3. 방문 순서 중요 : 정렬된 순서로 방문
4. 문자열 노드 : defaultdict로 키 관리
5. 스택 기반 구현 : 재귀 대신 반복문 사용
"""

"""
[자료구조]
1. adj_list: DefaultDict[str, List[str]]
   - 인접 리스트로 구현된 그래프
   - key: 노드, value: 인접 노드 리스트

2. visited: Set[str]
   - 방문한 노드들의 집합
   - O(1) 탐색을 위한 set 사용

[알고리즘: Iterative DFS]
procedure depth_first_search(graph, start):
    1. Initialize:
       - 인접 리스트 구성
       - 방문 집합과 결과 리스트 생성
       - 스택에 시작 노드 추가
    
    2. While stack not empty:
       - 현재 노드 처리
       - 미방문 이웃 노드들을 스택에 추가
       - 방문 순서 기록
    
    3. Return 방문 순서 리스트
"""

from collections import defaultdict, deque
from typing import List, Set, Dict, Any

def solution(graph: List[List[str]], start: str) -> List[str]:
    # 그래프를 인접 리스트로 변환 - defaultdict 활용하여 키 오류 방지
    adj_list = defaultdict(list)
    
    # 양방향 그래프 구성 - 더 유연한 탐색을 위해
    # DFS 자체는 방향과 무관한 탐색 알고리즘이지만, 주어진 그래프의 성질에 따라 단방향 또는 양방향으로 구현할 수 있습니다.
    # graph = {
    # 1: [2, 3],
    # 2: [4, 5],
    # 3: [],
    # 4: [],
    # 5: []
    # }
    for u, v in graph:
        adj_list[u].append(v)
        adj_list[v].append(u)  # 양방향 연결 추가
    
    # 반복적 DFS 구현 - 재귀 대신 스택 사용하여 콜 스택 오버플로우 방지
    def iterative_dfs(start_node: str) -> List[str]:
        visited: Set[str] = set()
        result: List[str] = []
        stack: deque = deque([start_node])
        
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                # 역순으로 스택에 추가하여 원하는 순서대로 방문
                for neighbor in sorted(adj_list[node], reverse=True):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result

    return iterative_dfs(start)

# TEST 코드
# print(solution([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A')) 
# print(solution([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A'))
