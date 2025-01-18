"""
[Input]
1. s: str
   - 0과 1로 이루어진 문자열
   - 제약: len(s) > 0
   - 제약: s는 '0'과 '1'로만 구성

[Output]
- result: List[int]
  - [변환 횟수, 제거된 0의 개수]
  - 제약: result[0] >= 0 (변환 횟수)
  - 제약: result[1] >= 0 (제거된 0의 개수)
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 문자열 내 특정 문자 제거 : count() 메서드 활용
2. 이진수 변환 필요 : bin() 함수 사용
3. 과정 반복 필요 : while 루프 구현
4. 두 가지 정보 추적 : 카운터 변수 사용
5. 종료 조건 존재 : "1" 도달 시 종료
"""
"""
[자료구조]
- transform_count: int
  - 목적: 변환 횟수 추적
  - 특징: 단순 증가 연산
- zero_count: int
  - 목적: 제거된 0의 개수 추적
  - 특징: 누적 덧셈

[알고리즘: String Transformation]
procedure transform_binary(s):
    1. Initialize:
       - transform_count = 0
       - zero_count = 0
    
    2. While s != "1":
       - count zeros in s
       - add to zero_count
       - remove zeros
       - convert length to binary
       - increment transform_count
    
    3. Return [transform_count, zero_count]
"""

def solution(s):
    # 최적화 1: 변환 횟수와 제거된 0의 개수 초기화
    transform_count = zero_count = 0
    
    # 최적화 2: 문자열이 "1"이 될 때까지 반복
    while s != "1":
        # 최적화 3: 현재 0의 개수 계산
        current_zeros = s.count("0")
        zero_count += current_zeros
        
        # 최적화 4: 1의 개수로 새로운 이진수 생성
        ones_count = len(s) - current_zeros
        s = bin(ones_count)[2:]  # "0b" 제거
        
        transform_count += 1
    
    return [transform_count, zero_count]

# 예시 실행
# print(solution("110010101001"))  # [3, 8]
# print(solution("01110"))  # [3, 3]
# print(solution("1111111"))  # [4, 1]
