"""
[Input]
1. amount: int
   - 거스름돈 금액
   - 제약: amount >= 0
   - 제약: amount는 정수

[Output]
- result: List[int]
  - 거스름돈으로 사용할 동전들의 배열
  - 제약: 각 원소는 [1, 10, 50, 100] 중 하나
  - 제약: 동전 개수가 최소가 되어야 함
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 최적 부분 구조 : 그리디 접근 가능
2. 큰 단위 우선 : 내림차순 처리
3. 단위 동전 제한 : 고정된 화폐 단위
4. 최소 개수 필요 : 큰 단위부터 처리
5. 나머지 처리 : 작은 단위로 보완
"""
"""
[자료구조]
- COINS: List[int]
  - 목적: 사용 가능한 동전 단위 저장
  - 특징: 내림차순 정렬 상태
  - 의미: [100, 50, 10, 1]

- result: List[int]
  - 목적: 선택된 동전들 저장
  - 특징: 동적 크기 배열
  - 갱신: 큰 단위부터 추가

[알고리즘: Greedy Coin Change]
procedure make_change(amount):
    1. Initialize:
       - 결과 배열 생성
       - 동전 단위 정의
    
    2. For each coin in COINS:
       - 현재 단위로 최대한 거슬러줌
       - 선택된 동전 추가
       - 남은 금액 갱신
    
    3. Return 선택된 동전들
"""

def solution(amount):
    # 최적화 1: 화폐 단위를 상수로 정의
    COINS = [100, 50, 10, 1]  # 내림차순으로 정렬된 상태
    
    # 최적화 2: 결과 리스트를 미리 할당하여 메모리 효율성 향상
    # @performance/append_vs_plus_performance.py 참조
    result = []
    
    # 최적화 3: 각 화폐 단위로 거스름돈 계산
    for coin in COINS:
        # 최적화 4: 현재 단위로 가능한 만큼 거스름돈 추가
        while amount >= coin:
            result.append(coin)
            amount -= coin
            
        # 최적화 5: 거스름돈이 0이 되면 조기 반환
        # @reference/early_return.py 참조
        if amount == 0:
            break
    
    return result

# 예시 실행
print(solution(123))  # [100, 10, 10, 1, 1, 1]
print(solution(350))  # [100, 100, 100, 50]
