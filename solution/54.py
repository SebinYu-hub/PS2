"""
[Input]
1. s: str
   - 알파벳 소문자로 이루어진 문자열
   - 제약: 1 <= len(s) <= 100,000
          s는 알파벳 소문자로만 구성

[Output]
- result: str
  - 알파벳 순으로 정렬된 문자열
  - 제약: len(result) == len(s)
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 알파벳 순서로 정렬 필요 : 카운팅 정렬로 O(N) 시간 복잡도 달성
2. 알파벳이 26개로 제한됨 : 고정 크기 배열로 빈도수 관리
3. 문자열 재구성 필요 : 빈도수 기반 문자열 생성
4. 입력이 소문자로 제한됨 : ASCII 코드 연산으로 간단한 인덱싱
5. 원본 순서 불필요 : 정렬된 순서만 유지하면 됨
"""
"""
[자료구조]
1. Frequency Array
   - 목적: 알파벳별 출현 빈도 저장
   - 특징: O(1) 접근, 26개 고정 크기

[알고리즘: Counting Sort]
procedure sort_string(s):
    initialize counts[26] with zeros
    
    for char in s:
        increment counts[char - 'a']
    
    build result string:
        for i in range(26):
            append char('a' + i) * counts[i]
    
    return result
"""

def solution(s):
    # 최적화 1: 알파벳 빈도수 배열을 0으로 초기화
    # @reference/list_comprehension.py 참조
    counts = [0] * 26
    
    # 최적화 2: 문자열 순회하며 빈도수 계산
    # ord() 함수로 문자를 아스키 코드로 변환
    for c in s:
        counts[ord(c) - ord('a')] += 1
    
    # 최적화 3: 결과 문자열 생성을 위한 리스트 사용
    result = []
    
    # 최적화 4: 알파벳 순서대로 빈도수만큼 문자 추가
    for i in range(26):
        # 최적화 5: chr() 함수로 아스키 코드를 문자로 변환
        if counts[i] > 0:
            result.append(chr(i + ord('a')) * counts[i])
    
    # 최적화 6: 리스트를 문자열로 결합
    # @performance/string_concatenation_performance.py 참조
    return ''.join(result)

# 예시 실행
# print(solution('hello'))  # 'ehllo'
# print(solution('algorithm'))  # 'aghilmort'
