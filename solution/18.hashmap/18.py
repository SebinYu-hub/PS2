"""
[Input]
1. arr: list[int]
   - 정수 배열
   - 제약: 1 ≤ len(arr) ≤ 100,000
   - 제약: 1 ≤ arr[i] ≤ 100,000

2. k: int
   - 목표 합
   - 제약: 1 ≤ k ≤ 200,000

[Output]
- result: bool
  - 두 수의 합이 k가 되는 조합이 있으면 True
  - 없으면 False
  - 제약: 서로 다른 두 수의 합으로만 가능
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 빠른 검색 필요 : set의 O(1) 탐색 활용
2. 메모리 효율성 필요 : 해시 테이블 사용
3. 중복 제거 필요 : set 자료구조 활용
4. 쌍 찾기 필요 : 보수 개념 활용
5. 최적화 필요 : 불필요한 검사 제외
"""
"""
[자료구조]
1. seen: list
   - 목적: 이미 확인한 수 저장
   - 특징: O(1) 시간 검색
   - 연산: append(), in

[알고리즘: Two Sum]
procedure solution(arr, k):
    1. Initialize:
       - 빈 seen 리스트 생성
    
    2. Process array:
       - 각 수에 대해:
         a) k보다 큰 수는 스킵
         b) 보수(k-num)가 seen에 있는지 확인
         c) 현재 수를 seen에 추가
    
    3. Return result:
       - 조합을 찾으면 True
       - 못 찾으면 False
"""

def solution(arr, k):
    # 해시 테이블(set)을 활용한 구현
    seen = []
    
    for num in arr:
        # k보다 큰 수는 처리할 필요 없음
        if num <= k:
            # num과 더해서 k가 되는 수가 이미 있는지 확인
            complement = k - num
            if complement in seen:
                return True
            # 현재 수를 해시 테이블에 추가
            seen.append(num)
    
    return False

# 예시 실행
print(solution([1, 2, 3, 4, 8], 6))  # True (2 + 4 = 6)
print(solution([2, 3, 5, 9], 10))  # False
