"""
[Input]
1. str1: str
   - 첫 번째 문자열
   - 제약: len(str1) > 0

2. str2: str
   - 두 번째 문자열
   - 제약: len(str2) > 0

[Output]
- result: int
  - 최장 공통 부분 수열(LCS)의 길이
  - 제약: 0 <= result <= min(len(str1), len(str2))
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 부분 문제 중복 발생 : DP 테이블 활용
2. 최적 부분 구조 존재 : 이전 결과 재사용
3. 메모리 최적화 필요 : 2행만 사용하는 DP
4. 문자열 비교 연산 : 인덱스 기반 접근
5. 최장 길이 계산 : 누적 최댓값 갱신
"""
"""
[자료구조]
- prev/curr: List[int]
  - 목적: DP 상태 저장
  - 특징: O(N) 공간으로 최적화

[알고리즘: LCS with Space Optimization]
procedure find_lcs(str1, str2):
    1. Initialize:
       - prev = [0] * (n+1)
       - curr = [0] * (n+1)
    
    2. For i in range(m):
       For j in range(n):
          if 문자 일치:
              curr[j] = prev[j-1] + 1
          else:
              curr[j] = max(prev[j], curr[j-1])
       prev, curr = curr, [0] * (n+1)
    
    3. Return prev[n]
"""

def solution(str1, str2):
    # 최적화 1: 문자열 길이 저장
    m, n = len(str1), len(str2)
    
    # 최적화 2: 메모리 사용량 최적화 - 2개의 행만 사용
    # @performance/for_loop_vs_list_comprehension.py 참조
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)
    
    # 최적화 3: LCS 길이 계산
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 최적화 4: 문자 비교 및 DP 값 갱신
            if str1[i - 1] == str2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        
        # 최적화 5: 다음 반복을 위해 행 교체
        prev, curr = curr, [0] * (n + 1)
    
    return prev[n]  # 최종 결과는 prev 배열의 마지막 값

# 예시 실행
# print(solution("ABCBDAB", "BDCAB"))  # 4
# print(solution("AGGTAB", "GXTXAYB"))  # 4
