#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# [실생활 예시] : [알고리즘 본질]
# 1. 웹 브라우저 방문기록 : 뒤로 가기 기능 구현
# 2. 문서 편집기 실행취소 : Ctrl+Z (undo) 기능
# 3. 괄호 검사기 : 프로그래밍 언어의 괄호 짝 맞추기


# [코딩테스트 꿀팁]
# 1. list로 구현
#    - append(): push 연산
#    - pop(): pop 연산
# 2. DFS에서 필수
#    - 재귀 대신 스택으로 구현
#    - 메모리 효율적
# 3. 괄호 문제에 활용
#    - 여는 괄호는 push
#    - 닫는 괄호는 pop 후 비교

# 스택 생성
stack = []

# Push 연산: 요소를 스택의 맨 위에 추가
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)  # 출력: [1, 2, 3, 4]

# Top 연산: 스택의 맨 위 요소 확인
print(stack[-1])  # 출력: 4

# Pop 연산: 스택의 맨 위 요소 삭제 및 반환
stack.pop()
print(stack)  # 출력: [1, 2, 3]

# 실제 활용 예시 - 괄호 짝 맞추기
def is_valid_parentheses(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in '({[':  # 여는 괄호
            stack.append(char)
        elif char in ')}]':  # 닫는 괄호
            if not stack or stack.pop() != brackets[char]:
                return False
    
    return len(stack) == 0

# 테스트
print(is_valid_parentheses("(){}[]"))  # 출력: True
print(is_valid_parentheses("([)]"))    # 출력: False
print(is_valid_parentheses("{[]}"))    # 출력: True
