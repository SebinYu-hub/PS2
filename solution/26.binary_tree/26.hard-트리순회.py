"""
[Input]
1. nodes: list[str]
   - 완전 이진 트리를 표현한 배열
   - 제약: 1 ≤ len(nodes) ≤ 10,000
   - 제약: 각 노드는 문자열 또는 숫자

[Output]
- result: list[str]
  - 세 가지 순회 결과를 담은 배열
  - 제약: [전위순회, 중위순회, 후위순회] 순서
  - 제약: 각 순회 결과는 공백으로 구분된 문자열
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 트리 순회 필요 : 재귀 함수 활용
2. 배열 기반 트리 : 인덱스 관계 활용
3. 세 가지 순회 필요 : 순회 함수 분리
4. 문자열 처리 필요 : 결과 포맷팅
5. 메모리 효율성 필요 : 문자열 연산 최적화
"""
"""
[자료구조]
1. nodes: list
   - 목적: 완전 이진 트리 표현
   - 특징: 인덱스로 부모-자식 관계 표현
   - 연산: 인덱스 접근

[알고리즘: Tree Traversal]
procedure solution(nodes):
    1. Preorder:
       - 루트 -> 왼쪽 -> 오른쪽 순서로 순회
       - 인덱스 관계로 자식 노드 접근
    
    2. Inorder:
       - 왼쪽 -> 루트 -> 오른쪽 순서로 순회
       - 재귀적으로 서브트리 처리
    
    3. Postorder:
       - 왼쪽 -> 오른쪽 -> 루트 순서로 순회
       - 결과 문자열 생성
"""

def preorder(nodes, idx):
    """전위 순회: 루트 -> 왼쪽 -> 오른쪽"""
    if idx >= len(nodes):
        return ""
    
    # 현재 노드와 그 자식 노드들의 순회 결과 조합
    return (f"{nodes[idx]} " + 
            preorder(nodes, 2*idx + 1) +  # 왼쪽 자식
            preorder(nodes, 2*idx + 2))   # 오른쪽 자식

def inorder(nodes, idx):
    """중위 순회: 왼쪽 -> 루트 -> 오른쪽"""
    if idx >= len(nodes):
        return ""
    
    # 왼쪽 서브트리, 현재 노드, 오른쪽 서브트리 순으로 조합
    return (inorder(nodes, 2*idx + 1) +   # 왼쪽 자식
            f"{nodes[idx]} " +            # 현재 노드
            inorder(nodes, 2*idx + 2))    # 오른쪽 자식

def postorder(nodes, idx):
    """후위 순회: 왼쪽 -> 오른쪽 -> 루트"""
    if idx >= len(nodes):
        return ""
    
    # 자식 노드들을 먼저 순회한 후 현재 노드 처리
    return (postorder(nodes, 2*idx + 1) +  # 왼쪽 자식
            postorder(nodes, 2*idx + 2) +  # 오른쪽 자식
            f"{nodes[idx]} ")              # 현재 노드

def solution(nodes):
    # 세 가지 순회 방식으로 트리를 순회하고 결과 반환
    # 마지막 공백 제거를 위해 strip() 사용
    return [
        preorder(nodes, 0).strip(),
        inorder(nodes, 0).strip(),
        postorder(nodes, 0).strip()
    ]

# 예시 실행
# print(solution([1, 2, 3, 4, 5, 6, 7]))
# 출력: ["1 2 4 5 3 6 7", "4 2 5 1 6 3 7", "4 5 2 6 7 3 1"]