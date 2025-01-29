"""
[Input]
1. items: List[List[int]]
   - 각 물건의 [무게, 가치]를 담은 2차원 배열
   - 제약: len(items) >= 1
   - 제약: items[i][0] > 0 (무게)
   - 제약: items[i][1] >= 0 (가치)

2. weight_limit: int
   - 배낭의 최대 무게 제한
   - 제약: weight_limit > 0

[Output]
- result: float
  - 배낭에 담을 수 있는 최대 가치
  - 제약: result >= 0.0
  - 제약: 물건을 쪼개서 담을 수 있음
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 분할 가능 배낭 : 그리디 접근 가능
2. 단위 가치 계산 : 가치/무게 비율
3. 최적 선택 필요 : 효율 기준 정렬
4. 부분 선택 가능 : 물건 쪼개기
5. 최대 가치 계산 : 순차적 처리
"""
"""
[자료구조]
- items: List[List[float]]
  - 목적: [무게, 가치, 단위가치] 저장
  - 특징: 단위가치 기준 정렬
  - 갱신: 내림차순 정렬

[알고리즘: Fractional Knapsack]
procedure find_max_value(items, weight_limit):
    1. Initialize:
       - 단위가치 계산 및 추가
       - 단위가치 기준 정렬
       - 결과값 초기화
    
    2. For each item:
       - 현재 물건을 최대한 담기
       - 필요시 물건 쪼개기
       - 가치 누적
    
    3. Return 최종 가치
"""

def solution(items, weight_limit):
    # 최적화 1: 단위 무게당 가치 계산 및 정렬
    # @reference/lambda.py 참조
    for item in items:
        item.append(item[1] / item[0])  # [무게, 가치, 단위가치]
    items.sort(key=lambda x: x[2], reverse=True)
    
    # 최적화 2: 최대 가치 계산
    total_value = 0
    remaining_weight = weight_limit
    
    # 최적화 3: 단위 가치가 높은 순서대로 처리
    for weight, value, _ in items:
        if remaining_weight >= weight:
            # 최적화 4: 물건을 통째로 선택
            total_value += value
            remaining_weight -= weight
        else:
            # 최적화 5: 남은 무게만큼만 분할하여 선택
            total_value += value * (remaining_weight / weight)
            break
    
    return total_value

# 예시 실행
# print(solution([[10, 19], [7, 10], [6, 10]], 15))  # 27.33...
# print(solution([[10, 60], [20, 100], [30, 120]], 50))  # 240.0
