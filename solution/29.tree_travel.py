"""
[트리 순회가 실생활에서 어떻게 쓰이는지 예시]

1. 디렉토리 크기 계산
실생활: 폴더의 전체 용량 계산
알고리즘 본질: 후위 순회로 하위 폴더 크기를 합산하여 상위 폴더 크기 계산

2. 수식 계산기
실생활: 수학 수식의 계산 순서 결정
알고리즘 본질: 중위 순회로 연산자 우선순위에 따른 계산 순서 결정

3. 조직도 출력
실생활: 회사 조직도를 계층적으로 출력
알고리즘 본질: 전위 순회로 상위자부터 순차적 출력

[자주 사용되는 파이썬 문법]
1. 클래스 정의
   class Node:
       def __init__(self, data):
           self.data = data
           self.left = self.right = None

2. 재귀 함수
   def recursive_function(node):
       if not node:
           return
       # 재귀 호출

[핵심 알고리즘 패턴 수도코드]

# 전위 순회 (Root -> Left -> Right)
def preorder(node):
    if not node:
        return
    process(node)
    preorder(node.left)
    preorder(node.right)

# 중위 순회 (Left -> Root -> Right)
def inorder(node):
    if not node:
        return
    inorder(node.left)
    process(node)
    inorder(node.right)

# 후위 순회 (Left -> Right -> Root)
def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    process(node)
"""

# 기존 코드는 유지... 