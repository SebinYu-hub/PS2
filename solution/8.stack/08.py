"""
[Input]
1. s: str
   - 괄호로 이루어진 문자열
   - 제약: 1 ≤ len(s) ≤ 100,000
   - 제약: s는 '(' 와 ')'로만 구성

[Output]
- result: bool
  - 올바른 괄호 문자열이면 true
  - 올바르지 않은 괄호 문자열이면 false
  - 제약: 빈 문자열은 올바른 괄호 문자열
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 괄호 짝 검사 필요 : 스택 자료구조 활용
2. LIFO 처리 필요 : 스택의 후입선출 특성 활용
3. 예외 처리 필요 : 빈 스택 검사
4. 순차 처리 필요 : 문자열 순회하며 검사
5. 최종 상태 확인 필요 : 스택이 비어있는지 확인
"""
"""
[자료구조]
1. stack: list
   - 목적: 여는 괄호 저장
   - 특징: LIFO(Last In First Out)
   - 연산: append(), pop()

[알고리즘: Parentheses Validation]
procedure solution(s):
    1. Initialize:
       - 빈 스택 생성
    
    2. Process string:
       - 각 문자에 대해:
         a) 여는 괄호면 스택에 추가
         b) 닫는 괄호면:
            - 스택이 비어있으면 false
            - 스택에서 pop
    
    3. Check final state:
       - 스택이 비어있으면 true
       - 아니면 false
"""

def solution(s):
    # 예시 입력값: s = "(())()"
    stack = []
    
    for char in s:
        if char == "(":  # 여는 괄호는 스택에 추가
            stack.append(char)
        else:  # 닫는 괄호 처리
            if not stack:  # 스택이 비어있으면 잘못된 경우
                return False
            stack.pop()  # 가장 최근의 여는 괄호 제거
    
    # 모든 괄호가 처리된 후 스택이 비어있어야 올바른 괄호 문자열
    return len(stack) == 0

# 예시 실행
# print(solution("(())()"))  # True
# print(solution("(()("))    # False
