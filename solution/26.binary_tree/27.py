"""
[Input]
1. lst: list[int]
   - 이진 탐색 트리에 삽입할 정수 배열
   - 제약: 1 ≤ len(lst) ≤ 10,000
   - 제약: 1 ≤ lst[i] ≤ 100,000

2. search_lst: list[int]
   - 검색할 정수 배열
   - 제약: 1 ≤ len(search_lst) ≤ 10,000
   - 제약: 1 ≤ search_lst[i] ≤ 100,000

[Output]
- result: list[bool]
  - 각 검색 값의 존재 여부 배열
  - 제약: len(result) == len(search_lst)
  - 제약: True는 존재, False는 미존재
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 정렬 유지 필요 : BST의 속성 활용
2. 효율적 검색 필요 : O(log N) 시간 복잡도
3. 동적 삽입 필요 : 노드 클래스로 구현
4. 순서 보존 필요 : 이진 탐색 트리 속성
5. 메모리 효율성 필요 : 포인터 기반 구현
"""
"""
[자료구조]
1. Node: class
   - 목적: BST의 노드 표현
   - 특징: 값과 좌우 포인터
   - 연산: 생성자

2. BST: class
   - 목적: 이진 탐색 트리 구현
   - 특징: 루트부터 탐색/삽입
   - 연산: insert, search

[알고리즘: Binary Search Tree]
procedure solution(lst, search_lst):
    1. Initialize BST:
       - 빈 BST 생성
       - lst의 값들을 순서대로 삽입
    
    2. Process searches:
       - 각 검색값에 대해:
         a) BST에서 값 검색
         b) 결과를 배열에 저장
    
    3. Return result:
       - 검색 결과 배열 반환
"""

class Node:
    """이진 탐색 트리의 노드 클래스"""
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BST:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """BST에 새로운 키 삽입"""
        if not self.root:
            self.root = Node(key)
            return

        curr = self.root
        while True:
            if key < curr.val:
                if not curr.left:
                    curr.left = Node(key)
                    break
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = Node(key)
                    break
                curr = curr.right

    def search(self, key):
        """BST에서 특정 키 검색"""
        curr = self.root
        while curr and curr.val != key:
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr is not None

def solution(lst, search_lst):
    # BST 생성 및 값 삽입
    bst = BST()
    for key in lst:
        bst.insert(key)
    
    # 검색 결과 리스트 생성
    return [bst.search(val) for val in search_lst]

# 예시 실행
# print(solution([5, 3, 8, 4, 2, 1, 7, 10], [1, 2, 5, 6]))  # [True, True, True, False]
# print(solution([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))  # [False, False, False, False, False]
