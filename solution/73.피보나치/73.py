"""
[Input]
1. n: int
   - 피보나치 수열의 인덱스
   - 제약: n >= 0
   - 제약: n은 정수

[Output]
- result: int
  - n번째 피보나치 수를 1234567로 나눈 나머지
  - 제약: 0 <= result < 1234567
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 큰 수 처리 필요 : 모듈러 연산 활용
2. 메모리 제한 존재 : 변수 두 개로 최적화
3. 이전 상태 활용 : 피보나치 수열 특성
4. 오버플로우 방지 : 중간 계산에서 모듈러
5. 반복적 계산 : 반복문 기반 구현
"""
"""
[알고리즘 선택 가이드: DP vs Greedy]

1. Greedy 알고리즘 선택 조건:
   - 최적 부분 구조(Optimal Substructure)와 탐욕 선택 속성이 있을 때
   - 현재의 최적 선택이 이후 선택에 영향을 주지 않음
   - 각 단계의 지역적 최적해가 전체의 최적해가 됨
   
   예시:
   - 거스름돈 (큰 단위부터)
   - 분할 가능 배낭 (단위 가치순)
   - 활동 선택 (종료 시간순)

2. DP 알고리즘 선택 조건:
   - 최적 부분 구조가 있고 중복되는 부분 문제가 존재할 때
   - 현재 선택이 이후 선택에 영향을 줌
   - 같은 계산이 반복적으로 필요함
   
   예시:
   - 0/1 배낭 (물건 분할 불가)
   - 최장 증가 부분 수열
   - 편집 거리

3. 구체적 판단 기준:
   a) 선택의 독립성
      - 독립적 → Greedy
      - 의존적 → DP
   
   b) 부분해의 최적성
      - 보장됨 → Greedy
      - 불확실 → DP
   
   c) 이전 선택의 영향
      - 영향 있음 → DP
      - 영향 없음 → Greedy
   
   d) 중복 계산 여부
      - 있음 → DP
      - 없음 → Greedy
"""
"""
[자료구조]
- prev, curr: int
  - 목적: 이전 두 피보나치 수 저장
  - 특징: 상수 공간만 사용

[알고리즘: Modular Fibonacci]
procedure find_fibonacci(n):
    1. Initialize:
       - 기본 케이스 처리 (n <= 1)
       - prev = 0, curr = 1 설정
    
    2. For i in range(2, n+1):
       - 다음 피보나치 수 계산
       - 모듈러 연산 적용
       - 변수 값 갱신
    
    3. Return 최종 결과
"""

def solution(n):
    # 최적화 1: 기본 케이스 처리
    if n <= 1:
        return n
        
    # 최적화 2: 두 개의 변수만 사용하여 메모리 절약
    # @performance/list_vs_deque_pop_performance.py 참조
    prev, curr = 0, 1
    
    # 최적화 3: 피보나치 수열 계산
    for _ in range(2, n + 1):
        # 최적화 4: 중간 계산에서 모듈러 연산 적용
        prev, curr = curr, (prev + curr) % 1234567
    
    return curr

# 예시 실행
# print(solution(3))   # 2
# print(solution(5))   # 5
# print(solution(100)) # 720955
