"""
[배열 기반 트리가 실생활에서 어떻게 쓰이는지 예시]

1. 토너먼트 대진표
실생활: 스포츠 토너먼트에서 선수들의 대진 구조
알고리즘 본질: 완전 이진 트리를 배열로 표현하여 O(1)로 부모/자식 접근

2. 우선순위 큐 구현(힙)
실생활: 응급실 환자 우선순위 시스템
알고리즘 본질: 배열로 구현된 힙을 통해 O(log n)으로 우선순위 관리

3. 조직도 표현
실생활: 고정된 크기의 부서/팀 구조
알고리즘 본질: 인덱스 기반으로 O(1)에 부모/자식 관계 접근

4. 게임 스킬트리
실생활: 게임의 스킬 계통도
알고리즘 본질: 선행 스킬과 후행 스킬의 관계를 배열 인덱스로 표현

[자주 사용되는 파이썬 문법]
1. 리스트 초기화
   tree = [None] * size  # 고정 크기 초기화
   tree = [None] + nodes  # 1-based 인덱싱용 더미 노드 추가

2. 인덱스 계산
   left = 2 * i  # 왼쪽 자식
   right = 2 * i + 1  # 오른쪽 자식
   parent = i // 2  # 부모 노드

[핵심 알고리즘 패턴 수도코드]

# 배열 기반 트리 생성
def create_array_tree(size):
    return [None] * (size + 1)  # 1-based 인덱싱

# 노드 관계 접근
def get_parent_idx(idx):
    return idx // 2

def get_children_idx(idx):
    return 2 * idx, 2 * idx + 1

# 트리 순회
def traverse_array_tree(tree, idx=1):
    if idx >= len(tree) or tree[idx] is None:
        return
    # 전위 순회
    process_node(tree[idx])
    traverse_array_tree(tree, 2 * idx)  # 왼쪽
    traverse_array_tree(tree, 2 * idx + 1)  # 오른쪽
"""

# 기존 코드는 유지... 