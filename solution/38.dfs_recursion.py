"""
[DFS 재귀가 실생활에서 어떻게 쓰이는지 예시]

1. 미로 찾기
실생활: 미로에서 출구까지의 경로 탐색
알고리즘 본질: 각 갈림길에서 한 방향으로 끝까지 탐색 후 백트래킹

2. 파일 시스템 검색
실생활: 특정 파일을 찾기 위해 폴더 깊숙이 탐색
알고리즘 본질: 재귀적으로 하위 디렉토리를 깊이 우선으로 탐색

3. 게임의 의사결정 트리
실생활: 체스 게임에서 수 읽기
알고리즘 본질: 각 수를 깊이 있게 따라가며 최적의 수 탐색

[자주 사용되는 파이썬 문법]
1. 재귀 함수 정의
   def dfs(params):
       if base_case:
           return
       # 재귀 호출

2. 방문 체크
   visited = set()  # 방문 기록용 집합
   visited.add(node)  # O(1) 방문 체크

[핵심 알고리즘 패턴 수도코드]

# DFS 재귀 구현
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    process(node)
    
    for next_node in graph[node]:
        if next_node not in visited:
            dfs_recursive(graph, next_node, visited)
"""

# 기존 코드는 유지... 