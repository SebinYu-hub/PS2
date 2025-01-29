"""
[Input]
1. N: int
   - 이진수로 변환할 자연수
   - 제약: N > 0

[Output]
- result: int
  - N의 이진수 표현에서 1의 개수
  - 제약: result >= 0
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 이진수 변환 필요 : bin() 함수 활용
2. 특정 문자 개수 세기 : count() 메서드 사용
3. 단순 계산 문제 : 내장 함수로 해결 가능
4. 결과값 단일 정수 : 직접 반환 가능
5. 최적화된 변환 필요 : 내장 함수 활용
"""
"""
[자료구조]
- 단순 변수만 사용
  - 목적: 이진수 변환과 카운팅
  - 특징: O(1) 공간 복잡도

[알고리즘: Binary Conversion]
procedure count_binary_ones(N):
    1. Convert N to binary string using bin()
    2. Count '1's in binary string
    3. Return count
"""

def solution(N):
    return bin(N).count('1')  # 2진수로 변환하고 1의 개수를 반환
