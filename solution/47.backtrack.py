# 백트랙킹(Backtracking)은 문제 해결 알고리즘의 하나로, 가능한 모든 해결책을 체계적으로 탐색하는 방법입니다.
# 주요 특징:
# 해결책을 찾아가는 도중 막히면, 이전 단계로 돌아가서(백트랙) 다른 경로를 탐색합니다
# DFS(깊이 우선 탐색) 방식을 기반으로 동작합니다
# 불필요한 경로를 조기에 차단(가지치기)하여 효율성을 높입니다


def backtrack(candidate):
    # 1.
    if is_solution(candidate):
        # 해답을 찾은 경우
        return candidate
    
    # 2.
    for next_candidate in get_possible_candidates(candidate):
        if is_valid(next_candidate):
            # 가능성 있는 후보 선택
            candidate.append(next_candidate)
            
            # 다음 단계로 재귀 진행
            result = backtrack(candidate)
            if result is not None:
                return result
                
            # 해답을 못찾았다면 백트랙 (선택 취소)
            candidate.pop()
    
    # 모든 후보를 시도해봤지만 해답이 없는 경우
    return None

# 사용 예시: [1,2,3] 중 합이 5가 되는 부분집합 찾기
def is_solution(candidate):
    return sum(candidate) == 5

def is_valid(next_num):
    return True  # 이 예제에서는 모든 숫자가 유효

def get_possible_candidates(candidate):
    numbers = [1, 2, 3]
    # 이미 사용된 숫자는 제외
    return [n for n in numbers if n not in candidate]

result = backtrack([])
print(result)  # [2, 3] 출력