"""
[Input]
1. nodeinfo: list[list[int]]
   - 각 노드의 [x, y] 좌표 배열
   - 제약: 1 ≤ len(nodeinfo) ≤ 10,000
   - 제약: 모든 좌표는 서로 다름
   - 제약: 0 ≤ x, y ≤ 100,000

[Output]
- result: list[list[int]]
  - [전위순회 결과, 후위순회 결과] 형태
  - 제약: 각 순회 결과는 노드 번호 배열
  - 제약: 노드 번호는 1부터 시작
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 좌표 기반 트리 : 위치 관계로 부모-자식 결정
2. 순회 구현 필요 : 스택으로 반복적 구현
3. 트리 구축 필요 : 노드 클래스 활용
4. 정렬 필요 : y좌표 내림차순, x좌표 오름차순
5. 메모리 효율성 필요 : 반복적 순회 구현
"""
"""
[자료구조]
1. Node: class
   - 목적: 이진 트리 노드 표현
   - 특징: 좌표 정보와 번호 저장
   - 연산: 생성자, 자식 노드 추가

2. nodes: list
   - 목적: 정렬된 노드 정보 저장
   - 특징: (번호, [x,y]) 튜플 저장
   - 연산: sort

[알고리즘: Binary Tree Construction]
procedure solution(nodeinfo):
    1. Initialize:
       - 노드 정보 정렬
       - 루트 노드 생성
    
    2. Build tree:
       - 각 노드를 위치에 따라 삽입
       - x좌표로 좌/우 결정
    
    3. Traverse tree:
       - 전위/후위 순회 수행
       - 결과 배열 생성
"""


class Node:
    """이진 트리 노드"""
    def __init__(self, info, num, left=None, right=None):
        self.info = info      # 노드의 좌표 정보
        self.num = num        # 노드의 번호
        self.left = left      # 왼쪽 자식 노드
        self.right = right    # 오른쪽 자식 노드

    def has_left(self):
        """왼쪽 자식 존재 여부"""
        return self.left is not None

    def has_right(self):
        """오른쪽 자식 존재 여부"""
        return self.right is not None

def make_BT(nodeinfo):
    """이진 트리 생성"""
    # 노드 번호 리스트 생성 및 y좌표 내림차순, x좌표 오름차순 정렬
    nodes = [(i+1, info) for i, info in enumerate(nodeinfo)]
    nodes.sort(key=lambda x: (-x[1][1], x[1][0]))
    
    if not nodes:
        return None
        
    root = Node(nodes[0][1], nodes[0][0])
    
    # 나머지 노드들을 트리에 삽입
    for num, info in nodes[1:]:
        parent = root
        node = Node(info, num)
        
        # 적절한 위치 찾아 삽입
        while True:
            if node.info[0] < parent.info[0]:  # 왼쪽 서브트리
                if not parent.has_left():
                    parent.left = node
                    break
                parent = parent.left
            else:  # 오른쪽 서브트리
                if not parent.has_right():
                    parent.right = node
                    break
                parent = parent.right
                
    return root

def pre_order(root, answer):
    """전위 순회 (반복적 구현)"""
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            answer[0].append(node.num)
            stack.append(node.right)  # 오른쪽 먼저 스택에 넣어
            stack.append(node.left)   # 왼쪽을 나중에 처리

def post_order(root, answer):
    """후위 순회 (반복적 구현)"""
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                answer[1].append(node.num)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

def solution(nodeinfo):
    answer = [[], []]
    root = make_BT(nodeinfo)
    pre_order(root, answer)
    post_order(root, answer)
    return answer

# 예시 실행
# nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
# print(solution(nodeinfo))


