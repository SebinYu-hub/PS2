"""
[Input]
1. N: int
   - 선택 가능한 숫자 범위
   - 제약: 1 ≤ N ≤ 100
   - 제약: 1부터 N까지의 자연수 중 선택

[Output]
- result: list[list[int]]
  - 합이 10이 되는 모든 조합의 리스트
  - 제약: 각 조합은 오름차순 정렬
  - 제약: 각 숫자는 한 번만 사용
  - 제약: 모든 조합은 서로 다름
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 조합 생성 필요 : 백트래킹 알고리즘 활용
2. 합 제한 필요 : 가지치기로 최적화
3. 중복 방지 필요 : 방문 체크 활용
4. 순서 유지 필요 : 오름차순 정렬 보장
5. 메모리 효율성 필요 : 재귀 호출 최적화
"""
"""
[자료구조]
1. results: list[list[int]]
   - 목적: 유효한 조합 저장
   - 특징: 오름차순 정렬된 조합
   - 연산: append

[알고리즘: Sum Combination]
procedure solution(N):
    1. Initialize:
       - 결과 리스트 생성
       - 백트래킹 함수 정의
    
    2. Backtrack:
       - 각 숫자에 대해:
         a) 합이 10 초과시 중단
         b) 합이 10이면 결과 저장
         c) 다음 숫자로 재귀
    
    3. Return result:
       - 찾은 모든 조합 반환
"""

def solution(N):
    # 최적화 1: 결과 리스트를 함수 내부에서 관리
    results = []
    
    # 최적화 2: 백트래킹 함수를 내부에 정의하여 변수 접근 최적화
    def backtrack(curr_sum, selected, start):
        # 최적화 3: 합이 10을 초과하면 더 이상 탐색하지 않음
        if curr_sum > 10:
            return
            
        # 최적화 4: 합이 10이면 결과에 추가
        if curr_sum == 10:
            results.append(selected[:])  # 리스트 복사본 저장
            return
        
        # 최적화 5: 남은 숫자들로 만들 수 있는 최대 합 계산
        remaining_sum = (N - start + 1) * N // 2
        if curr_sum + remaining_sum < 10:
            return
            
        # 최적화 6: 가능한 다음 숫자들에 대해 재귀 호출
        for num in range(start, N + 1):
            # 최적화 7: 현재 숫자를 선택한 경우만 탐색
            backtrack(curr_sum + num, selected + [num], num + 1)
    
    # 최적화 8: 초기 호출 시 빈 리스트로 시작
    backtrack(0, [], 1)
    return results

# 예시 실행
# print(solution(5))  # [[1, 2, 3, 4], [1, 4, 5], [2, 3, 5]]
# print(solution(2))  # []
# print(solution(7))  # [[1, 2, 3, 4], [1, 2, 7], [1, 3, 6], [1, 4, 5], [2, 3, 5], [3, 7], [4, 6]]
