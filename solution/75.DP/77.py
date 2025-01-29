"""
[Input]
1. money: List[int]
   - 각 집에 있는 돈의 양을 담은 배열
   - 제약: len(money) >= 1
   - 제약: 각 원소는 0 이상의 정수
   - 제약: 첫 집과 마지막 집은 서로 인접

[Output]
- result: int
  - 도둑이 훔칠 수 있는 돈의 최대값
  - 제약: result >= 0
  - 제약: 인접한 두 집을 연속해서 털 수 없음
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 원형 배열 처리 : 두 가지 경우로 분리
2. 인접 선택 제한 : DP로 상태 관리
3. 최적 부분 구조 : DP 접근 가능
4. 메모리 최적화 : 변수 두 개로 해결
5. 두 가지 시나리오 : 첫 집 선택 여부
"""
"""
[자료구조]
- prev2, prev1: int
  - 목적: 이전 두 상태값 저장
  - 특징: 상수 공간만 사용
  - 갱신: 슬라이딩 윈도우 방식

[알고리즘: Circular House Robbery]
procedure find_max_money(money):
    1. Initialize:
       - 기본 케이스 처리 (len <= 3)
       - 두 가지 시나리오 설정
    
    2. For each scenario:
       - 첫 집 포함/미포함 각각 계산
       - DP로 최대값 갱신
       - 변수 슬라이딩
    
    3. Return max(두 시나리오의 결과)
"""

def solution(money):
    # 최적화 1: 두 개의 변수만 사용하여 메모리 절약
    # @performance/list_vs_deque_pop_performance.py 참조
    def get_max_money(start, end):
        prev2, prev1 = 0, money[start]
        
        # 최적화 2: 각 위치에서 최대값 계산
        for i in range(start + 1, end):
            # 최적화 3: 현재 위치에서 가능한 최대값 계산
            curr = max(prev1, prev2 + money[i])
            prev2, prev1 = prev1, curr
        
        return prev1
    
    # 최적화 4: 첫 집을 털 경우와 안 털 경우로 분리
    if len(money) <= 3:
        return max(money)
        
    # 최적화 5: 두 경우 중 최대값 반환
    return max(
        get_max_money(0, len(money) - 1),  # 첫 집을 터는 경우
        get_max_money(1, len(money))       # 첫 집을 안 터는 경우
    )

# 예시 실행
# print(solution([1, 2, 3, 1]))  # 4
# print(solution([1, 1, 4, 1, 4]))  # 8
