"""
[Input]
1. n: int
   - 참여하는 사람 수
   - 2 ≤ n ≤ 10

2. words: List[str]
   - 순서대로 말한 단어들
   - 2 ≤ len(words) ≤ 100
   - 모든 단어는 알파벳 소문자

[Output]
- result: List[int] [번호, 차례]
  - 탈락하는 사람의 번호와 차례
  - [0, 0]: 탈락자가 없는 경우
"""

"""
[문제 특징] : [알고리즘 선택 이유]
1. 중복 단어 체크 필요 : set으로 이미 사용된 단어 관리
2. 끝말잇기 규칙 검사 : 문자열 인덱싱으로 첫/끝 글자 비교
3. 순환 구조 계산 : 나머지 연산으로 번호/차례 계산
4. 빠른 탐색 필요 : set의 O(1) 탐색 활용
5. early return 가능 : 실패 조건 즉시 반환
"""

"""
[자료구조]
1. used_words: Set[str]
   - 사용된 단어 저장
   - O(1) 탐색을 위한 set 사용

[알고리즘: Word Chain Game]
procedure find_failure(n, words):
    1. Initialize:
       - 첫 단어 used_words에 추가
    
    2. For each word:
       - 이전 단어 끝글자와 현재 첫글자 비교
       - 중복 단어 체크
       - 실패시 [번호, 차례] 반환
    
    3. Return [0, 0] if no failure
"""

def solution(n, words):
    # 최적화 1: early return 패턴 적용
    # 첫 단어는 무조건 통과하므로 used_words에 미리 추가
    used_words = {words[0]}
    
    # 최적화 2: 반복문 범위 축소 (첫 단어 제외)
    for i in range(1, len(words)):
        # 실패 조건을 먼저 체크하여 early return
        if words[i] in used_words or words[i][0] != words[i-1][-1]:
            return [(i % n) + 1, (i // n) + 1]
        used_words.add(words[i])
    
    return [0, 0]

# TEST 코드입니다
# print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream"]))  # [3, 3]
# print(solution(2, ["hello", "one", "even", "never", "now", "world"]))  # [1, 3]
