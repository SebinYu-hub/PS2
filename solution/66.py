from collections import Counter

def solution(topping):
    """
    [Input]
    1. topping: List[int]
       - 토핑 종류가 담긴 배열
       - 제약: len(topping) > 0
       - 제약: 각 원소는 토핑 종류를 나타내는 양의 정수

    [Output]
    - result: int
      - 롤케이크를 공평하게 자르는 방법의 수
      - 제약: result >= 0
      - 제약: 각 조각의 토핑 종류 수가 같아야 함
    """
    """
    [문제 특징] : [알고리즘 선택 이유]
    1. 토핑 종류 카운팅 필요 : Counter 자료구조 활용
    2. 양쪽 토핑 비교 필요 : Set으로 중복 제거
    3. 모든 자르는 위치 확인 : 선형 순회 필요
    4. 동적인 토핑 개수 관리 : Counter 증감 연산
    5. 빈도수 관리 필요 : 해시맵 기반 접근
    """
    """
    [자료구조]
    - right_counter: Counter
      - 목적: 오른쪽 토핑 종류별 개수 관리
      - 특징: O(1) 접근/수정
    - left_set: Set
      - 목적: 왼쪽 토핑 종류 관리
      - 특징: O(1) 탐색/추가

    [알고리즘: Two Pointers with Counter]
    procedure find_fair_cuts(topping):
        1. Initialize:
           - right_counter로 전체 토핑 개수 계산
           - left_set 빈 집합으로 초기화
           - result = 0
        
        2. For each t in topping:
           - left_set에 토핑 추가
           - right_counter에서 토핑 제거
           - if 양쪽 토핑 종류 수 같으면:
               result 증가
        
        3. Return result
    """
    
    # 최적화 1: Counter로 전체 토핑 개수 계산
    # @reference/counter.py 참조
    right_counter = Counter(topping)
    
    # 최적화 2: 왼쪽 토핑 종류를 저장할 set
    # @performance/list_vs_set_in.py 참조
    left_set = set()
    result = 0
    
    # 최적화 3: 토핑을 하나씩 옮기며 개수 비교
    for t in topping:
        # 최적화 4: 왼쪽에 토핑 추가
        left_set.add(t)
        
        # 최적화 5: 오른쪽에서 토핑 제거
        right_counter[t] -= 1
        if right_counter[t] == 0:
            right_counter.pop(t)
        
        # 최적화 6: 양쪽 토핑 종류 수 비교
        if len(left_set) == len(right_counter):
            result += 1
    
    return result

# 예시 실행
# print(solution([1, 2, 1, 3, 1, 4, 1, 2]))  # 2
# print(solution([1, 2, 3, 1, 4]))  # 0
