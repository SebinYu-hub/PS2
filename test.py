"""
백트랙킹

해결책 찾는도중 막히면 되돌아가기
💥DFS 기반
💥불필요한 경로 나오면 조기에 차단 -> 다시 돌아가기
"""

def backtracking(candidate): #💥0. candidate는 보통 리스트 자료구조
    # 1.
    if is_solution(candidate):
        return candidate
    
    # 2.솔루션 아니여서 - 다음 경로 진행
    for next_candidate in get_possible_candidates(candidate):
        #💥 3.다음 경로 갈 조건인지
        if is_vaild(next_candidate):
            #💥 4.다음 탐색 후보 추가
            candidate.append(next_candidate)

            #💥 5.다음 탐색 시킴 - 찾아오면 해당 턴 종료
            result = backtracking(candidate)
            if result is not None:
                return result
            
            #💥 6.못찾아오면 next_candidate 추가했던거 빠빠이
            candidate.pop()

    # 어느것도 해당하지 않으면
    return None