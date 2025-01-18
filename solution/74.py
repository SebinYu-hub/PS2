"""
[Input]
1. n: int
   - 가로 길이
   - 제약: n >= 1
   - 제약: n은 정수

[Output]
- result: int
  - 2x1, 1x2 타일로 채우는 방법의 수를 1000000007로 나눈 나머지
  - 제약: 0 <= result < 1000000007
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 점화식 패턴 존재 : 피보나치 수열 응용
2. 큰 수 처리 필요 : 모듈러 연산 활용
3. 메모리 제한 존재 : 변수 두 개로 최적화
4. 이전 상태 활용 : DP 접근 필요
5. 반복적 패턴 : 반복문 기반 구현
"""
"""
[자료구조]
- prev, curr: int
  - 목적: 이전 두 상태값 저장
  - 특징: 상수 공간만 사용
  - 의미: 이전 위치까지의 방법 수

[알고리즘: Tiling DP]
procedure find_tiling_ways(n):
    1. Initialize:
       - 기본 케이스 처리 (n <= 2)
       - prev = 1, curr = 2 설정
    
    2. For i in range(3, n+1):
       - 다음 상태값 계산
       - 모듈러 연산 적용
       - 변수 값 갱신
    
    3. Return 최종 결과
"""

def solution(n):
    # 최적화 1: 기본 케이스 처리
    # @reference/early_return.py 참조
    if n <= 2:
        return n
    
    # 최적화 2: 두 개의 변수만 사용하여 메모리 절약
    # @performance/list_vs_deque_pop_performance.py 참조
    prev, curr = 1, 2
    MOD = 1000000007
    
    # 최적화 3: 타일링 경우의 수 계산
    for _ in range(3, n + 1):
        # 최적화 4: 중간 계산에서 모듈러 연산 적용
        prev, curr = curr, (prev + curr) % MOD
    
    return curr

# 예시 실행
# print(solution(4))  # 5
# print(solution(3))  # 3
