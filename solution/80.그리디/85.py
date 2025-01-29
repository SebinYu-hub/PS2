"""
[Input]
1. N: int
   - 아파트 개수
   - 제약: 1 ≤ N ≤ 200,000,000

2. stations: List[int]
   - 기존 기지국 위치 배열
   - 제약: 1 ≤ stations[i] ≤ N
   - 제약: 오름차순 정렬 상태

3. W: int
   - 전파 도달 거리
   - 제약: 1 ≤ W ≤ 10,000
"""
"""
[Output]
- result: int
  - 추가로 필요한 기지국 수
  - 제약: result ≥ 0
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 구간 커버 필요 : 그리디 접근
2. 연속된 범위 : 구간 처리
3. 최소 개수 요구 : 최적 위치 선정
4. 기존 설치 고려 : 미커버 구간 계산
5. 거리 기반 : 범위 계산
"""
"""
[자료구조]
- uncovered: List[List[int]]
  - 목적: 미커버 구간 저장
  - 특징: [시작, 끝] 형태
  - 처리: 순차적 계산

[알고리즘: Greedy Station Installation]
procedure install_stations(N, stations, W):
    1. Initialize:
       - 미커버 구간 리스트
       - 현재 위치 포인터
    
    2. For each station:
       - 이전 구간 끝 ~ 현재 범위 시작
       - 미커버 구간 추가
       - 다음 시작 위치 갱신
    
    3. Calculate:
       - 각 미커버 구간별
       - 필요한 기지국 수 계산
    
    4. Return 총 필요 기지국 수
"""

def solution(N, stations, W):
    # 최적화 1: 기지국이 커버하지 않는 구간 계산
    uncovered = []
    start = 1
    
    # 최적화 2: 기존 기지국들의 커버리지 계산
    for station in stations:
        if start < station - W:
            uncovered.append([start, station - W - 1])
        start = station + W + 1
    
    # 최적화 3: 마지막 구간 처리
    if start <= N:
        uncovered.append([start, N])
    
    # 최적화 4: 필요한 기지국 수 계산
    coverage = 2 * W + 1  # 하나의 기지국이 커버하는 범위
    answer = 0
    
    # 최적화 5: 각 커버되지 않은 구간에 대해 필요한 기지국 수 계산
    for start, end in uncovered:
        distance = end - start + 1
        # 최적화 6: 올림 나눗셈으로 필요한 기지국 수 계산
        answer += (distance + coverage - 1) // coverage
    
    return answer

# 예시 실행
# print(solution(11, [4, 11], 1))  # 3
# print(solution(16, [9], 2))  # 3
