"""
[Input]
1. n: int
   - 화살의 개수
   - 제약: 1 <= n <= 10

2. info: List[int]
   - 어피치가 맞힌 과녁 점수 정보
   - 길이 11의 배열 (0~10점)
   - 제약: 각 원소는 0 이상의 정수

[Output]
- result: List[int]
  - 라이언이 가장 큰 점수 차이로 이기기 위한 과녁 점수
  - 길이 11의 배열 (0~10점 과녁에 대한 화살 개수)
  - 각 원소는 해당 점수에 맞힌 화살의 개수
  - 모든 원소의 합은 n과 같아야 함
  - 가장 큰 점수 차이로 이기는 방법이 여러 가지일 경우:
    - 가장 낮은 점수를 더 많이 맞힌 경우를 선택
  - 라이언이 이길 수 없는 경우 [-1] 반환
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 상태 공간이 크고 제약이 있는 탐색 문제
   - 백트래킹으로 가지치기하며 효율적 탐색
   - 불가능한 경우(화살 초과)는 즉시 중단

2. 각 점수(0-10)마다 선택적 결정 필요
   - 해당 점수 획득 시도 vs 포기
   - 어피치보다 많이 쏘거나 아예 안 쏘는 것이 최적

3. 최적해 보장 필요
   - 백트래킹으로 모든 유효한 경우 탐색
   - 전역 변수로 최대 점수차 관리

4. 여러 최적해 중 특정 조건 충족 필요
   - 같은 점수차일 때 낮은 점수 우선
   - 배열 간 비교로 사전순 처리

5. 자원 제약 조건 존재
   - n발의 화살을 정확히 모두 사용
   - 남은 화살은 0점에 할당하여 조건 충족
"""
"""

[자료구조]
1. Counter
   - 목적: 각 점수별 화살 개수 관리
   - 특징: O(1) 접근, 개수 비교 용이

[알고리즘: Combinations with Replacement]
procedure find_max_score_difference(n, info):
    initialize max_difference, best_combination
    
    # combinations_with_replacement(range(11), n)는 0~10 중에서 n개를 중복을 허용하여 뽑는 모든 조합을 생성
    # 예: n=2일 때 (0,0), (0,1), (1,1), (0,2), (1,2), (2,2) 등의 조합 생성
    # 화살을 n발 쏠 때 각 점수에 몇 발씩 배분할지의 모든 경우의 수를 표현
    for combination in combinations_with_replacement(range(11), n):
        1. Counter로 화살 개수 계산
        2. 어피치와 점수 비교하여 차이 계산
        3. 최대 점수 차이 갱신
           - 같은 차이면 낮은 점수가 많은 경우 선택
    
    if no winning case:
        return [-1]
    return best_combination
"""

from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    def backtrack(arrows_left, current_score, idx, current):
        nonlocal max_diff, answer
        
        # 기저 사례: 모든 점수를 고려했거나 화살을 다 사용한 경우
        if idx == 11 or arrows_left == 0:
            # 남은 화살이 있다면 0점에 모두 할당
            if arrows_left > 0:
                current[10] = arrows_left
            
            # 점수 계산
            apeach, ryan = 0, 0
            for i in range(11):
                if info[i] > 0 or current[i] > 0:
                    if info[i] >= current[i]:
                        apeach += 10 - i
                    else:
                        ryan += 10 - i
            
            # 최대 점수 차이 갱신
            diff = ryan - apeach
            if diff > 0 and diff >= max_diff:
                if diff > max_diff or current > answer:
                    max_diff = diff
                    answer[:] = current[:]
            
            # 남은 화살 처리 원상복구
            if arrows_left > 0:
                current[10] = 0
            return
        
        # 현재 점수에 화살을 쏘는 경우
        if arrows_left > info[idx]:
            current[idx] = info[idx] + 1
            backtrack(arrows_left - (info[idx] + 1), current_score + (10 - idx), idx + 1, current)
            current[idx] = 0
        
        # 현재 점수를 포기하는 경우
        backtrack(arrows_left, current_score, idx + 1, current)
    
    max_diff = 0
    answer = [0] * 11
    backtrack(n, 0, 0, [0] * 11)
    
    return answer if max_diff > 0 else [-1]

# 예시 실행
# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))  # [0,2,2,0,1,0,0,0,0,0,0]
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))  # [-1]
