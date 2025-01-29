"""
[Input]
1. prices: list[int]
   - 초 단위로 기록된 주식 가격 배열
   - 제약: 2 ≤ len(prices) ≤ 100,000
   - 제약: 1 ≤ prices[i] ≤ 10,000

[Output]
- result: list[int]
  - 각 시점부터 가격이 떨어지지 않은 기간을 담은 배열
  - 제약: len(result) == len(prices)
  - 제약: 마지막 가격은 항상 0 기간
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 가격 하락 시점 추적 필요 : 단조 감소 스택 활용
2. 시간 간격 계산 필요 : 인덱스 차이로 계산
3. 효율적 연산 필요 : deque로 최적화
4. 이전 상태 참조 필요 : 스택의 top과 비교
5. 남은 기간 처리 필요 : 마지막 시점 기준 계산
"""
"""
[자료구조]
1. stack: deque
   - 목적: 가격과 시점 저장
   - 특징: 단조 감소 스택
   - 연산: append(), pop()

2. answer: list
   - 목적: 각 시점별 유지 기간 저장
   - 특징: 인덱스로 시점 매핑
   - 크기: prices 길이와 동일

[알고리즘: Price Duration]
procedure solution(prices):
    1. Initialize:
       - 결과 배열 생성
       - 빈 스택 생성
    
    2. Process prices:
       - 각 시점에 대해:
         a) 현재 가격이 스택 top보다 작으면:
            - 스택에서 pop하며 기간 계산
         b) 현재 시점과 가격을 스택에 추가
    
    3. Handle remaining:
       - 스택에 남은 가격들 처리
       - 마지막 시점 기준으로 기간 계산
"""

from collections import deque

def solution(prices):
    # 예시 입력값: prices = [1, 2, 3, 2, 3]
    n = len(prices)
    answer = [0] * n  # 가격이 떨어지지 않은 기간을 저장할 배열
    
    # deque를 사용하여 스택 연산 최적화
    stack = deque()  # (가격, 시점) 저장할 스택
    
    # 모든 가격을 한 번씩만 순회 (최적화 1)
    for curr_time, curr_price in enumerate(prices):
        # 현재 가격이 스택의 top 가격보다 작다면, 가격이 떨어진 시점
        while stack and prices[stack[-1]] > curr_price:
            prev_time = stack.pop()
            answer[prev_time] = curr_time - prev_time
        
        stack.append(curr_time)
    
    # 남은 시간 계산 최적화 (최적화 2)
    last_time = n - 1
    while stack:
        prev_time = stack.pop()
        answer[prev_time] = last_time - prev_time
        
    return answer

# 예시 실행
# prices = [1, 2, 3, 2, 3]
# 과정 설명:
# 1초: stack = [0]                   -> answer = [0, 0, 0, 0, 0]
# 2초: stack = [0, 1]                -> answer = [0, 0, 0, 0, 0]
# 3초: stack = [0, 1, 2]             -> answer = [0, 0, 0, 0, 0]
# 4초: stack = [0, 1, 3] (2 pop)     -> answer = [0, 0, 1, 0, 0]
# 5초: stack = [0, 1, 3, 4]          -> answer = [0, 0, 1, 1, 0]
# 끝: stack 비우기                    -> answer = [4, 3, 1, 1, 0]

# print(solution([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]
# print(solution([5, 4, 3, 2, 1]))  # [1, 1, 1, 1, 0]
