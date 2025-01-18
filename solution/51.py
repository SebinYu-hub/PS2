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
  - 길이 11의 배열
  - 불가능한 경우 [-1]
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 모든 가능한 화살 배분을 고려해야 함 : 중복조합으로 모든 경우 탐색
2. 점수 계산 시 어피치와 비교 필요 : Counter로 효율적인 개수 비교
3. 최대 점수 차이를 찾아야 함 : 완전탐색으로 최적해 보장
4. 같은 점수일 때 가장 낮은 점수 많이 맞힌 경우 선택 : 정렬 기준 설정
5. n발의 화살을 모두 사용해야 함 : 조합 생성 시 제약조건 추가
"""
"""
[자료구조]
1. Counter
   - 목적: 각 점수별 화살 개수 관리
   - 특징: O(1) 접근, 개수 비교 용이

[알고리즘: Combinations with Replacement]
procedure find_max_score_difference(n, info):
    initialize max_difference, best_combination
    
    for combination in combinations_with_replacement(0~10, n):
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
    # 최적화 1: 함수를 내부에 정의하여 변수 접근 최적화
    def calculate_score(combi):
        # 최적화 2: 점수 계산을 한번에 처리
        score1, score2 = 0, 0
        for i in range(1, 11):
            if info[10 - i] < combi.count(i):
                score1 += i
            elif info[10 - i] > 0:
                score2 += i
        return score1, score2
    
    # 최적화 3: 최대 차이 계산 함수 분리
    def calculate_diff(diff, cnt):
        nonlocal maxdiff, max_comb
        if diff > maxdiff:
            max_comb = cnt
            maxdiff = diff
    
    # 최적화 4: 변수 초기화를 함수 시작 부분에서 처리
    maxdiff, max_comb = 0, {}
    
    # 최적화 5: combinations_with_replacement로 중복 조합 생성
    # @reference/combination_direct.py 참조
    for combi in combinations_with_replacement(range(11), n):
        # 최적화 6: Counter로 화살 개수 계산
        cnt = Counter(combi)
        score1, score2 = calculate_score(combi)
        diff = score1 - score2
        calculate_diff(diff, cnt)
    
    # 최적화 7: list comprehension으로 결과 배열 생성
    if maxdiff > 0:
        return [max_comb[n] if n in max_comb else 0 for n in range(10, -1, -1)]
    return [-1]

# 예시 실행
# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))  # [0,2,2,0,1,0,0,0,0,0,0]
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))  # [-1]
