"""
[Input]
1. brown: int
   - 갈색 격자의 수
   - 제약: brown > 0
   - 제약: brown은 카펫 테두리를 이룸

2. yellow: int
   - 노란색 격자의 수
   - 제약: yellow >= 0
   - 제약: yellow는 카펫 내부를 이룸

[Output]
- result: List[int]
  - [가로 길이, 세로 길이]
  - 제약: result[0] >= result[1] (가로 >= 세로)
  - 제약: 테두리는 갈색, 내부는 노란색
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 약수 쌍 찾기 필요 : 제곱근까지만 탐색
2. 조건 만족 검증 필요 : 테두리/내부 격자수 계산
3. 최적해 하나만 존재 : 조건 만족 시 즉시 반환
4. 가로/세로 관계 존재 : 가로 >= 세로 조건
5. 격자 수 계산 필요 : 수식 기반 검증
"""
"""
[자료구조]
- 단순 변수만 사용
  - 목적: 약수 쌍과 결과 저장
  - 특징: O(1) 공간 복잡도

[알고리즘: Factor Pair Search]
procedure find_carpet_size(brown, yellow):
    1. total = brown + yellow
    2. For height in range(3, sqrt(total) + 1):
       if total % height == 0:
           width = total // height
           if (width-2) * (height-2) == yellow:
               return [width, height]
    3. Return [] (no solution found)
"""

def solution(brown, yellow):
    # 최적화 1: 전체 격자 수 계산
    total = brown + yellow
    
    # 최적화 2: 제곱근까지만 탐색하여 약수 쌍 찾기
    # @performance/for_loop_vs_list_comprehension.py 참조
    for height in range(3, int(total ** 0.5) + 1):
        # 최적화 3: 약수인 경우만 처리
        if total % height == 0:
            width = total // height
            
            # 최적화 4: 카펫 조건 검사
            if (width - 2) * (height - 2) == yellow:
                return [width, height]
    
    return []  # 조건을 만족하는 크기가 없는 경우

# 예시 실행
# print(solution(10, 2))  # [4, 3]
# print(solution(8, 1))   # [3, 3]
# print(solution(24, 24)) # [8, 6]
