"""
[Input]
1. s: str
   - 대괄호, 중괄호, 소괄호로 이루어진 문자열
   - 제약: 1 ≤ len(s) ≤ 1,000
   - 제약: s는 '[]{}()'로만 구성

[Output]
- result: int
  - 올바른 괄호 문자열이 되는 회전 횟수
  - 제약: 0 ≤ result ≤ len(s)
  - 제약: 회전은 왼쪽으로 한 칸씩 이동
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 문자열 회전 필요 : deque의 rotate 활용
2. 괄호 검증 필요 : 스택 자료구조 활용
3. 괄호 매핑 필요 : 딕셔너리로 쌍 관리
4. 여러 유형 처리 필요 : set으로 괄호 종류 구분
5. 반복 검사 필요 : 모든 회전에 대해 검증
"""
"""
[자료구조]
1. s_deque: deque
   - 목적: 문자열 회전 처리
   - 특징: O(1) 시간 회전 연산

2. stack: list
   - 목적: 괄호 검증
   - 특징: LIFO 구조

3. brackets: dict
   - 목적: 괄호 쌍 매핑
   - 특징: O(1) 시간 매칭 확인

[알고리즘: Rotating Brackets]
procedure solution(s):
    1. Initialize:
       - deque로 문자열 변환
       - 괄호 매핑 정의
       - 여는/닫는 괄호 set 생성
    
    2. For each rotation:
       - 현재 상태에서 괄호 유효성 검사
       - 유효하면 카운트 증가
       - 문자열 왼쪽으로 회전
    
    3. Return count:
       - 유효한 회전 수 반환
"""

from collections import deque

def solution(s):
    # 예시 입력값: s = "[](){}"
    n = len(s)
    answer = 0
    
    # 괄호 매핑과 set으로 빠른 검사
    brackets = {')': '(', '}': '{', ']': '['}
    opening = set("({[")  # 여는 괄호 set
    closing = set(")}]")  # 닫는 괄호 set
    
    # 문자열을 deque로 변환하여 효율적인 회전 구현
    s_deque = deque(s)
    
    # 모든 회전 위치에 대해 검사
    for _ in range(n):
        stack = []
        is_valid = True
        
        # 현재 회전 상태에서 괄호 검사
        for char in s_deque:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if not stack or stack[-1] != brackets[char]:
                    is_valid = False
                    break
                stack.pop()
        
        if is_valid and not stack:
            answer += 1
            
        # 다음 회전을 위해 효율적으로 회전
        s_deque.rotate(-1)
            
    return answer

# 예시 실행
# print(solution("[](){}"))  # 3
# print(solution("}]()[{"))  # 2
# print(solution("[)(]"))    # 0
