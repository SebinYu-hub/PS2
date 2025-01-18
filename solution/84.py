from collections import Counter

def solution(k, tangerine):
    """
    [Input]
    1. k: int
       - 선택해야 할 귤의 개수
       - 제약: 1 ≤ k ≤ len(tangerine)

    2. tangerine: List[int]
       - 귤의 크기 배열
       - 제약: 1 ≤ tangerine[i] ≤ 10,000,000
       - 제약: 1 ≤ len(tangerine) ≤ 100,000
    """
    """
    [Output]
    - result: int
      - 최소 크기 종류 수
      - 제약: result > 0
    """
    """
    [문제 특징] : [알고리즘 선택 이유]
    1. 크기별 개수 필요 : Counter 활용
    2. 최소 종류 요구 : 그리디 접근
    3. 빈도수 기반 : 정렬 필요
    4. 부분 선택 : 누적 합 계산
    5. 개수 우선 : 내림차순 처리
    """
    """
    [자료구조]
    - size_counts: Counter
      - 목적: 크기별 빈도수 저장
      - 특징: {크기: 개수} 형태
      - 정렬: 값 기준 내림차순

    [알고리즘: Greedy Size Selection]
    procedure select_sizes(k, tangerine):
        1. Initialize:
           - Counter로 빈도수 계산
           - 빈도수 내림차순 정렬
        
        2. For each frequency:
           - 누적 개수 계산
           - 목표 개수 도달 확인
           - 종류 수 카운트
        
        3. Return 최소 종류 수
    """
    
    # 최적화 1: Counter로 크기별 개수 계산
    # @reference/counter.py 참조
    size_counts = Counter(tangerine)
    
    # 최적화 2: 개수를 기준으로 내림차순 정렬
    counts = sorted(size_counts.values(), reverse=True)
    
    # 최적화 3: 필요한 최소 종류 수 계산
    total = 0
    for i, count in enumerate(counts):
        total += count
        if total >= k:
            return i + 1
    
    return len(counts)  # k가 전체 귤의 개수보다 작거나 같은 경우

# 예시 실행
# print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))  # 3
# print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))  # 2
