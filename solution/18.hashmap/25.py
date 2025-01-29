"""
[Input]
1. orders: list[str]
   - 각 손님이 주문한 단품메뉴 배열
   - 제약: 2 ≤ len(orders) ≤ 20
   - 제약: 2 ≤ len(orders[i]) ≤ 10

2. course: list[int]
   - 코스요리를 구성하는 단품메뉴 개수 배열
   - 제약: 1 ≤ len(course) ≤ 10
   - 제약: 2 ≤ course[i] ≤ 10

[Output]
- result: list[str]
  - 추천 코스요리의 메뉴 구성 배열
  - 제약: 최소 2명 이상의 손님이 주문한 조합만
  - 제약: 각 코스요리는 오름차순으로 정렬
  - 제약: 메뉴 구성은 알파벳 오름차순으로 정렬
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 조합 생성 필요 : combinations 활용
2. 빈도수 계산 필요 : Counter 클래스 활용
3. 길이별 처리 필요 : course 길이별로 분리 처리
4. 최대 빈도 선택 필요 : max() 함수로 최빈값 추출
5. 정렬 필요 : sorted()로 알파벳 순 정렬
"""
"""
[자료구조]
1. order_combinations: list
   - 목적: 가능한 메뉴 조합 저장
   - 특징: 정렬된 문자열로 저장
   - 연산: extend, join

2. combination_counts: Counter
   - 목적: 조합별 주문 횟수 저장
   - 특징: 해시 테이블 기반
   - 연산: most_common()

[알고리즘: Menu Combination]
procedure solution(orders, course):
    1. Generate combinations:
       - 각 주문에 대해 course 길이별 조합 생성
       - 정렬하여 순서 통일
    
    2. Count frequencies:
       - 각 조합의 등장 횟수 계산
       - 최소 2회 이상 등장한 조합만 선택
    
    3. Select best combinations:
       - 각 길이별로 가장 많이 주문된 조합 선택
       - 알파벳 순으로 정렬하여 반환
"""

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for length in course:
        # 각 주문에서 가능한 모든 length 길이의 조합 생성
        order_combinations = []
        for order in orders:
            # 정렬하여 순서 통일
            sorted_order = ''.join(sorted(order))
            # 현재 길이의 모든 조합 생성
            order_combinations.extend(
                ''.join(combo) 
                for combo in combinations(sorted_order, length)
            )
        
        # 조합별 등장 횟수 계산
        combination_counts = Counter(order_combinations)
        
        # 가장 많이 주문된 조합 찾기
        if combination_counts:
            max_count = max(combination_counts.values())
            if max_count >= 2:  # 최소 2명 이상의 손님이 주문한 조합만
                answer.extend(
                    combo for combo, count in combination_counts.items()
                    if count == max_count
                )
    
    return sorted(answer)  # 알파벳 순으로 정렬하여 반환

# 예시 실행
# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2,3,4]
# print(solution(orders, course))  # ["AC", "ACDE", "BCFG", "CDE"]
