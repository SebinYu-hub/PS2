"""
[DFS 스택이 실생활에서 어떻게 쓰이는지 예시]

1. 웹 크롤링
실생활: 웹사이트의 모든 링크를 깊이 우선으로 수집
알고리즘 본질: 스택으로 방문할 링크를 관리하며 깊이 우선 탐색

2. 작업 스케줄링
실생활: 작업의 선행 관계를 고려한 실행 순서 결정
알고리즘 본질: 의존성 그래프를 DFS로 탐색하여 위상 정렬

3. SNS 관계 탐색
실생활: 특정 사용자로부터 시작하여 친구 관계 탐색
알고리즘 본질: 스택으로 방문할 사용자를 관리하며 깊이 우선 탐색

[자주 사용되는 파이썬 문법]
1. 스택 구현
   stack = []  # 빈 스택 생성
   stack.append(item)  # O(1) 푸시
   item = stack.pop()  # O(1) 팝

2. 방문 체크
   visited = [False] * n  # 방문 배열
   visited[node] = True  # 방문 표시

[핵심 알고리즘 패턴 수도코드]

# DFS 스택 구현
def dfs_stack(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            process(node)
            stack.extend(neighbor for neighbor in graph[node]
                        if neighbor not in visited)
"""

# 기존 코드는 유지... 