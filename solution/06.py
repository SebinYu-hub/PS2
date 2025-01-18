"""
[Input]
1. N: int
   - 전체 스테이지의 개수
   - 제약: 1 ≤ N ≤ 500

2. stages: list[int]
   - 사용자가 현재 도전 중인 스테이지 번호 배열
   - 제약: 1 ≤ len(stages) ≤ 200,000
   - 제약: 1 ≤ stages[i] ≤ N+1
   - 제약: N+1은 마지막 스테이지 클리어를 의미

[Output]
- result: list[int]
  - 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담긴 배열
  - 제약: 실패율이 같은 스테이지는 작은 번호가 먼저 옴
  - 제약: 도달한 유저가 없는 스테이지의 실패율은 0
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 빈도수 계산 필요 : Counter 클래스 활용
2. 실패율 계산 필요 : defaultdict로 0 처리 자동화
3. 정렬 기준 복잡 : 튜플 키를 활용한 다중 정렬
4. 누적 계산 필요 : 변수로 누적값 추적
5. 예외 처리 필요 : 분모가 0인 경우 처리
"""
"""
[자료구조]
1. stage_counts: Counter
   - 목적: 각 스테이지별 도전자 수 저장
   - 특징: 해시 테이블 기반 O(1) 접근

2. failure_rates: defaultdict
   - 목적: 각 스테이지별 실패율 저장
   - 특징: 키 없을 때 자동으로 0 할당

[알고리즘: Failure Rate Calculation]
procedure solution(N, stages):
    1. Count challengers:
       - Counter로 각 스테이지 도전자 수 계산
    
    2. Calculate failure rates:
       - 각 스테이지 순회하며 실패율 계산
       - total_players 변수로 분모 관리
       - 실패율 = 현재 도전자 / 총 도달자
    
    3. Sort stages:
       - 실패율 내림차순, 스테이지 번호 오름차순으로 정렬
       - (-failure_rates[x], x) 형태의 키 사용
"""

from collections import Counter, defaultdict

def solution(N, stages):
    # 최적화 1: Counter로 각 스테이지별 도전자 수를 효율적으로 계산
    stage_counts = Counter(stages)
    print(Counter(stages))
    # 최적화 2: defaultdict로 실패율 저장 (KeyError 방지)
    failure_rates = defaultdict(float)
    total_players = len(stages)
    
    # 최적화 3: 각 스테이지의 실패율을 한 번의 순회로 계산
    for stage in range(1, N + 1):
        if total_players > 0:
            current_players = stage_counts[stage]  # 없으면 0 반환
            failure_rates[stage] = current_players / total_players
            total_players -= current_players
    
    # 최적화 4: 실패율 내림차순, 스테이지 번호 오름차순으로 정렬
    return sorted(range(1, N + 1), key=lambda x: (-failure_rates[x], x))

# 예시 실행
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))  # [3, 4, 2, 1, 5]
print(solution(4, [4, 4, 4, 4, 4]))  # [4, 1, 2, 3]
