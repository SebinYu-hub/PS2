"""
[Input]
1. strs: List[str]
   - 문자열 조각들의 배열
   - 제약: len(strs) >= 1
   - 제약: 각 문자열은 영소문자로만 구성

2. t: str
   - 만들어야 할 목표 문자열
   - 제약: len(t) >= 1
   - 제약: 영소문자로만 구성

[Output]
- result: int
  - 목표 문자열을 만들기 위한 최소 조각 개수
  - 제약: result >= -1 (-1은 불가능한 경우)
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 부분 문자열 매칭 : Set으로 조각 관리
2. 최적 부분 구조 : DP 접근 가능
3. 중복 계산 발생 : 메모이제이션 필요
4. 문자열 검색 최적화 : 길이별 조각 분류
5. 최소값 갱신 : DP로 최소 개수 관리
"""
"""
[자료구조]
- pieces_by_len: Dict[int, Set[str]]
  - 목적: 길이별 문자열 조각 저장
  - 특징: O(1) 검색 가능
  - 최적화: 길이별 분류로 검색 범위 축소

- dp: List[int]
  - 목적: 각 위치까지의 최소 조각 수 저장
  - 특징: 초기값 무한대로 설정
  - 갱신: 가능한 모든 조각 시도

[알고리즘: String Pieces DP]
procedure find_min_pieces(strs, t):
    1. Initialize:
       - 길이별 조각 분류
       - DP 배열 초기화
       - 기본 케이스 처리
    
    2. For each position in t:
       - 가능한 모든 길이의 조각 시도
       - 매칭되는 조각 찾기
       - 최소 조각 수 갱신
    
    3. Return 최종 최소값 (불가능하면 -1)
"""

def solution(strs, t):
    # 최적화 1: 문자열 길이와 DP 배열 초기화
    n = len(t)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    # 최적화 2: 조각들을 길이별로 분류하여 검색 최적화
    # @performance/list_vs_set_in.py 참조
    pieces_by_len = {}
    for s in strs:
        length = len(s)
        if length not in pieces_by_len:
            pieces_by_len[length] = set()
        pieces_by_len[length].add(s)
    
    # 최적화 3: 각 위치까지의 최소 조각 수 계산
    for i in range(1, n + 1):
        # 최적화 4: 실제 존재하는 조각 길이만 검사
        for length in pieces_by_len:
            if i >= length:
                # 최적화 5: 현재 위치에서 가능한 조각 확인
                piece = t[i-length:i]
                if piece in pieces_by_len[length]:
                    dp[i] = min(dp[i], dp[i-length] + 1)
    
    # 최적화 6: 불가능한 경우 처리
    return dp[n] if dp[n] != float('inf') else -1

# 예시 실행
# print(solution(["ba","na","n","a"], "banana"))  # 3
# print(solution(["app","ap","p","l","e","ple","pp"], "apple"))  # 2
