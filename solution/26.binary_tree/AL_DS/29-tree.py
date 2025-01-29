"""
[트리 알고리즘이 실생활에서 어떻게 쓰이는지 예시]

1. 계층적 데이터 관리
실생활: 회사의 조직도 시스템
알고리즘 본질: 부모-자식 관계를 트리로 표현하여 O(log n) 탐색

2. 파일 시스템
실생활: 컴퓨터의 디렉토리 구조
알고리즘 본질: 재귀적 구조를 트리로 표현하여 효율적 탐색/관리

3. 의사결정 시스템
실생활: 고객 상담 시스템의 질문 흐름도
알고리즘 본질: 각 결정을 노드로 표현하여 최적 경로 탐색

[자주 사용되는 파이썬 문법]
1. 딕셔너리 기반 트리
   tree = {parent: [children]}  # 하향식
   tree = {child: parent}      # 상향식

2. 재귀 함수
   def traverse(node):
       if not node: return
       # 재귀 처리

3. 레벨 관리
   level = {}
   level[node] = level[parent] + 1

[핵심 알고리즘 패턴 수도코드]

# 1. 상향식(Bottom-up) 패턴들

# 1-1. 조상 찾기
def find_ancestor(node, k, parent_map):
    current = node
    for _ in range(k):
        if current not in parent_map:
            return None
        current = parent_map[current]
    return current

# 1-2. 공통 조상 찾기
def find_common_ancestor(node1, node2, parent_map):
    ancestors = set()
    while node1:
        ancestors.add(node1)
        node1 = parent_map.get(node1)
    while node2:
        if node2 in ancestors:
            return node2
        node2 = parent_map.get(node2)
    return None

# 1-3. 노드 깊이 계산
def get_depth(node, parent_map):
    depth = 0
    current = node
    while current in parent_map:
        depth += 1
        current = parent_map[current]
    return depth

# 2. 하향식(Top-down) 패턴들

# 2-1. 서브트리 크기 계산
def subtree_size(node, children_map):
    if node not in children_map:
        return 1
    return 1 + sum(subtree_size(child, children_map) 
                  for child in children_map[node])

# 2-2. 최대 깊이 찾기
def max_depth(node, children_map):
    if node not in children_map:
        return 0
    return 1 + max((max_depth(child, children_map) 
                    for child in children_map[node]), default=0)

# 2-3. 경로 존재 여부 확인
def path_exists(start, end, children_map):
    if start == end:
        return True
    return any(path_exists(child, end, children_map) 
              for child in children_map.get(start, []))

# 3. 레벨 기반 패턴들

# 3-1. 레벨별 노드 그룹화
def group_by_level(root, children_map):
    levels = defaultdict(list)
    queue = deque([(root, 0)])
    
    while queue:
        node, level = queue.popleft()
        levels[level].append(node)
        for child in children_map.get(node, []):
            queue.append((child, level + 1))
    return levels

# 3-2. 특정 레벨의 모든 노드 찾기
def find_nodes_at_level(root, target_level, children_map):
    if target_level == 0:
        return [root]
    
    result = []
    def dfs(node, current_level):
        if current_level == target_level:
            result.append(node)
            return
        for child in children_map.get(node, []):
            dfs(child, current_level + 1)
    
    dfs(root, 0)
    return result
"""

# 기존 코드는 유지... 