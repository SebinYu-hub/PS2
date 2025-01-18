"""
[Input]
1. s: str
   - 영문 소문자로 이루어진 문자열
   - 제약: 1 ≤ len(s) ≤ 1,000,000
   - 제약: s는 알파벳 소문자로만 구성

[Output]
- result: int
  - 모든 문자를 제거할 수 있으면 1
  - 모든 문자를 제거할 수 없으면 0
  - 제약: 연속된 같은 문자 2개를 제거
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 연속 문자 처리 필요 : 스택 자료구조 활용
2. 문자 제거 필요 : 스택의 pop 연산 활용
3. 효율적 연산 필요 : deque로 최적화
4. 상태 추적 필요 : 스택의 top 값 비교
5. 최종 검증 필요 : 스택이 비어있는지 확인
"""
"""
[자료구조]
1. stack: deque
   - 목적: 문자 쌓기와 제거
   - 특징: O(1) 시간 push/pop
   - 연산: append(), pop()

[알고리즘: Character Elimination]
procedure solution(s):
    1. Initialize:
       - 빈 스택 생성
    
    2. Process string:
       - 각 문자에 대해:
         a) 스택이 비어있지 않고 top이 현재 문자와 같으면:
            - pop 수행
         b) 그렇지 않으면:
            - 현재 문자를 push
    
    3. Check result:
       - 스택이 비어있으면 1
       - 아니면 0
"""

from collections import deque

def solution(s):
    # 예시 입력값: s = "baabaa"
    stack = deque()  # deque를 스택으로 활용하여 pop/append 연산 최적화
    
    for c in s:
        if stack and stack[-1] == c:  # 스택이 비어있지 않고, 현재 문자와 스택의 맨 위 문자가 같으면
            stack.pop()   # 스택의 맨 위 문자 제거
        else:
            stack.append(c)  # 스택에 현재 문자 추가
            
    return int(not stack)  # 스택이 비어있으면 1, 그렇지 않으면 0 반환

# 예시 실행
# print(solution("baabaa"))  # 1 (모든 문자가 제거됨)
# print(solution("cdcd"))    # 0 (제거되지 않는 문자가 남음)
