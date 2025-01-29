"""
[트리의 인접 리스트 표현이 실생활에서 어떻게 쓰이는지 예시]

1. 회사의 조직도 표현
실생활: CEO -> 부서장 -> 팀장 -> 팀원으로 이어지는 조직도
알고리즘 본질: 계층적 구조를 인접 리스트로 표현하여 O(1)로 부하 직원 접근

2. 파일 시스템 구조
실생활: 폴더와 하위 폴더, 파일들의 계층 구조
알고리즘 본질: 트리의 각 노드(폴더)가 자식 노드들(하위 폴더/파일)의 리스트를 가짐

3. 가족 관계도
실생활: 조상-자손 관계를 표현하는 가계도
알고리즘 본질: 각 노드가 자식 노드들의 리스트를 가지며 O(1)로 자식 탐색

[자주 사용되는 파이썬 문법]
1. 딕셔너리 생성과 접근
   tree = {}  # 빈 딕셔너리 생성
   tree[key] = []  # 리스트를 값으로 가지는 딕셔너리
   children = tree.get(node, [])  # 기본값 처리

2. 리스트 조작
   children.append(child)  # O(1) 추가
   for child in children:  # 순회

[핵심 알고리즘 패턴 수도코드]

# 인접 리스트 트리 생성
def create_tree():
    tree = {}
    for node in nodes:
        tree[node] = []  # 각 노드의 자식 리스트 초기화
    return tree

# 노드 추가
def add_node(tree, parent, child):
    if parent not in tree:
        tree[parent] = []
    if child not in tree:
        tree[child] = []
    tree[parent].append(child)

# 트리 순회
def traverse_tree(tree, root):
    if not root:
        return
    # 현재 노드 처리
    process_node(root)
    # 자식 노드 순회
    for child in tree[root]:
        traverse_tree(tree, child)
"""

# 기존 코드는 유지... 