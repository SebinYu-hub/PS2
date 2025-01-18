"""
[Input]
1. d: List[int]
   - 각 부서별 신청 금액 배열
   - 제약: 1 ≤ d[i] ≤ 100,000
   - 제약: 1 ≤ len(d) ≤ 100

2. budget: int
   - 총 예산
   - 제약: 1 ≤ budget ≤ 10,000,000
"""
"""
[Output]
- result: int
  - 지원 가능한 최대 부서 수
  - 제약: 0 ≤ result ≤ len(d)
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 최대 부서 수 필요 : 그리디 접근 가능
2. 작은 금액 우선 : 정렬 후 처리
3. 예산 제한 : 누적 합 계산
4. 순차적 처리 : 반복문 한번으로 해결
5. 부분 최적해 : 전체 최적해 보장
"""
"""
[자료구조]
- d: List[int]
  - 목적: 부서별 신청 금액 저장
  - 특징: 오름차순 정렬 필요
  - 갱신: 정렬만 수행, 내부 값 변경 없음

[알고리즘: Greedy Budget Distribution]
procedure distribute_budget(d, budget):
    1. Initialize:
       - 배열 오름차순 정렬
       - 누적 합 변수 초기화
    
    2. For each amount in sorted array:
       - 현재 금액 누적
       - 예산 초과 검사
       - 가능한 경우 계속 진행
    
    3. Return 지원 가능한 부서 수
"""

def solution(d, budget):
    # 최적화 1: 신청 금액 오름차순 정렬
    # @reference/sorting_methods_comparison.py 참조
    d.sort()
    
    # 최적화 2: 누적 합 계산으로 성능 향상
    # @performance/for_loop_vs_list_comprehension.py 참조
    cumsum = 0
    for i, amount in enumerate(d):
        cumsum += amount
        # 최적화 3: 예산 초과 시 이전 인덱스 반환
        if cumsum > budget:
            return i
        # 최적화 4: 마지막 요소까지 예산이 충분한 경우
        if i == len(d) - 1:
            return len(d)
    
    # 최적화 5: 빈 배열인 경우 처리
    return 0

# 예시 실행
# print(solution([1,3,2,5,4], 9))  # 3
# print(solution([2,2,3,3], 10))  # 4
