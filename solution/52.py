"""
[Input]
1. n: int
   - 외벽의 길이
   - 제약: 5 <= n <= 200

2. weak: List[int]
   - 취약 지점의 위치
   - 제약: 1 <= len(weak) <= 15
          0 <= weak[i] < n

3. dist: List[int]
   - 각 친구가 이동할 수 있는 거리
   - 제약: 1 <= len(dist) <= 8
          1 <= dist[i] <= 100

[Output]
- result: int
  - 필요한 최소 친구 수
  - 불가능한 경우 -1
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 친구들의 순서가 결과에 영향 : 순열로 모든 순서 탐색
2. 원형 외벽을 선형으로 처리해야 함 : 배열 확장으로 선형화
3. 각 취약점을 누가 점검할지 결정 필요 : 그리디로 최적 할당
4. 모든 취약점을 커버해야 함 : 완전탐색으로 모든 경우 확인
5. 최소 인원을 찾아야 함 : 가능한 모든 조합 중 최솟값 탐색
"""
"""
[자료구조]
1. Extended Array
   - 목적: 원형 배열을 선형으로 변환
   - 특징: 2배 길이로 확장하여 순환 처리

[알고리즘: Permutation + Linear Search]
procedure find_min_friends(n, weak, dist):
    extend weak points array to handle circular nature
    initialize answer = len(dist) + 1
    
    for start in range(len(weak)):
        for friends_order in permutations(dist):
            1. 현재 시작점에서 친구들 배치
            2. 각 친구가 커버할 수 있는 취약점 확인
            3. 모든 취약점이 커버되면 최소 인원 갱신
    
    return answer if answer <= len(dist) else -1
"""

from itertools import permutations

def solution(n, weak, dist):
    # 최적화 1: 원형 배열을 선형으로 변환
    length = len(weak)
    # @reference/list_comprehension.py 참조
    linear_weak = weak + [w + n for w in weak]
    
    # 최적화 2: 초기값을 불가능한 값으로 설정
    answer = len(dist) + 1
    
    # 최적화 3: 시작점을 기준으로 모든 경우 탐색
    for start in range(length):
        # 최적화 4: 순열로 모든 순서 생성
        # @reference/permutation_direct.py 참조
        for friends in permutations(dist):
            count = 1  # 투입 인원 수
            position = weak[start] + friends[0]  # 현재 위치
            
            # 최적화 5: 다음 취약점까지 도달 가능 여부 확인
            for idx in range(start, start + length):
                if position < linear_weak[idx]:
                    count += 1
                    if count > len(dist):  # 불가능한 경우
                        break
                    position = linear_weak[idx] + friends[count - 1]
            
            # 최적화 6: 최소 인원 갱신
            answer = min(answer, count)
    
    # 최적화 7: 불가능한 경우 처리
    return answer if answer <= len(dist) else -1

# 예시 실행
# print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))  # 2
# print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))  # 1
