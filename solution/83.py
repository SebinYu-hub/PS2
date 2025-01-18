"""
[Input]
1. people: List[int]
   - 사람들의 몸무게 배열
   - 제약: 40 ≤ people[i] ≤ 240
   - 제약: 1 ≤ len(people) ≤ 50,000

2. limit: int
   - 구명보트 무게 제한
   - 제약: 40 ≤ limit ≤ 240
"""
"""
[Output]
- result: int
  - 필요한 구명보트의 최소 개수
  - 제약: result > 0
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 최소 보트 수 필요 : 그리디 접근
2. 양쪽 끝 비교 필요 : 투 포인터 활용
3. 무게 제한 존재 : 조건부 이동
4. 2인 1조 제한 : 페어링 처리
5. 최적 매칭 필요 : 정렬 후 처리
"""
"""
[자료구조]
- people: List[int]
  - 목적: 사람들의 무게 저장
  - 특징: 오름차순 정렬 필요
  - 접근: 양쪽 끝에서 중앙으로

[알고리즘: Two Pointer Boat Assignment]
procedure assign_boats(people, limit):
    1. Initialize:
       - 배열 오름차순 정렬
       - 양쪽 포인터 설정
       - 보트 수 카운터
    
    2. While left <= right:
       - 양쪽 무게 합 계산
       - 조건부 포인터 이동
       - 보트 수 증가
    
    3. Return 필요한 보트 수
"""

def solution(people, limit):
    # 최적화 1: 무게 오름차순 정렬
    # @reference/sorting_methods_comparison.py 참조
    people.sort()
    
    # 최적화 2: 투 포인터 초기화
    i = 0  # 가장 가벼운 사람 인덱스
    j = len(people) - 1  # 가장 무거운 사람 인덱스
    count = 0  # 필요한 보트 개수
    
    # 최적화 3: 양쪽에서 접근하며 보트 수 계산
    while i <= j:
        # 최적화 4: 가장 가벼운 사람과 무거운 사람이 함께 탈 수 있는 경우
        if people[j] + people[i] <= limit:
            i += 1
        # 최적화 5: 무거운 사람 혼자 타야 하는 경우
        j -= 1
        count += 1
    
    return count

# 예시 실행
# print(solution([70, 50, 80, 50], 100))  # 3
# print(solution([70, 80, 50], 100))  # 3
