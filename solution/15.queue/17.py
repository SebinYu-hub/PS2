"""
[Input]
1. cards1: list[str]
   - 첫 번째 카드 뭉치
   - 제약: 1 ≤ len(cards1) ≤ 10
   - 제약: 카드는 알파벳 소문자로만 구성

2. cards2: list[str]
   - 두 번째 카드 뭉치
   - 제약: 1 ≤ len(cards2) ≤ 10
   - 제약: 카드는 알파벳 소문자로만 구성

3. goal: list[str]
   - 만들고자 하는 단어 배열
   - 제약: 1 ≤ len(goal) ≤ len(cards1) + len(cards2)
   - 제약: goal의 단어는 cards1과 cards2의 단어로만 구성

[Output]
- result: str
  - 목표 문자열을 만들 수 있으면 "Yes"
  - 만들 수 없으면 "No"
  - 제약: 카드는 순서대로만 사용 가능
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 순차적 처리 필요 : deque의 popleft 활용
2. 두 배열 비교 필요 : 양쪽 카드뭉치 동시 처리
3. 효율적 접근 필요 : O(1) 시간 연산 활용
4. 순서 유지 필요 : 카드 순서 그대로 사용
5. 조건 검사 필요 : 매 단계 유효성 확인
"""
"""
[자료구조]
1. cards1/cards2: deque
   - 목적: 카드 뭉치 관리
   - 특징: 앞에서부터 순차 접근
   - 연산: popleft()

2. goal: deque
   - 목적: 목표 단어 순서 관리
   - 특징: 순차적 검증 가능
   - 연산: popleft()

[알고리즘: Card Sequence]
procedure solution(cards1, cards2, goal):
    1. Initialize:
       - 모든 배열을 deque로 변환
    
    2. Process goal:
       - 각 목표 단어에 대해:
         a) cards1 첫 단어와 일치하면 cards1에서 제거
         b) cards2 첫 단어와 일치하면 cards2에서 제거
         c) 둘 다 아니면 "No" 반환
    
    3. Return result:
       - 모든 단어 처리 완료시 "Yes"
"""

from collections import deque

def solution(cards1, cards2, goal):
    # 각 카드 뭉치와 목표 문자열을 deque로 변환
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    
    # goal의 각 단어를 순서대로 처리
    while goal:
        current_word = goal[0]
        
        # cards1의 첫 번째 카드가 현재 목표 단어와 일치하는 경우
        if cards1 and cards1[0] == current_word:
            cards1.popleft()
            goal.popleft()
        # cards2의 첫 번째 카드가 현재 목표 단어와 일치하는 경우
        elif cards2 and cards2[0] == current_word:
            cards2.popleft()
            goal.popleft()
        # 어느 카드 뭉치에서도 현재 단어를 만들 수 없는 경우
        else:
            return "No"
    
    # 모든 목표 단어를 순서대로 만들 수 있는 경우
    return "Yes"

# 예시 실행
# print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))  # "Yes"
# print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))  # "No"
