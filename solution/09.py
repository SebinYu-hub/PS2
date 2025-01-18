"""
[Input]
1. decimal: int
   - 변환할 10진수
   - 제약: 0 ≤ decimal ≤ 1,000,000
   - 제약: decimal은 정수

[Output]
- result: str
  - decimal을 2진수로 변환한 문자열
  - 제약: 앞에 불필요한 0이 없어야 함
  - 제약: 음수가 아닌 정수만 처리
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 진법 변환 필요 : 나머지(%) 연산 활용
2. 역순 처리 필요 : 스택 자료구조 활용
3. 특수 케이스 처리 필요 : 0 입력 처리
4. 문자열 조작 필요 : join() 메서드 활용
5. 메모리 효율성 필요 : 리스트로 결과 구성
"""
"""
[자료구조]
1. binary: list
   - 목적: 2진수 자릿수 저장
   - 특징: 역순으로 구성됨
   - 연산: append(), reverse()

[알고리즘: Binary Conversion]
procedure solution(decimal):
    1. Handle special case:
       - 입력이 0이면 "0" 반환
    
    2. Convert to binary:
       - decimal이 0보다 큰 동안:
         a) 2로 나눈 나머지를 저장
         b) decimal을 2로 나눈 몫으로 갱신
    
    3. Build result:
       - 저장된 나머지들을 역순으로 문자열로 변환
       - join으로 결합
"""

def solution(decimal):
    # 예시 입력값: decimal = 10
    if decimal == 0:  # 0은 특별 케이스로 처리
        return "0"
        
    # bin() 내장 함수 사용 대신 직접 구현
    binary = []
    while decimal > 0:
        binary.append(str(decimal % 2))  # 나머지를 문자열로 변환하여 추가
        decimal //= 2  # 몫 갱신
        
    # 이진수는 역순으로 읽어야 함
    return ''.join(reversed(binary))

# 예시 실행
# print(solution(10))    # "1010"
# print(solution(27))    # "11011"
# print(solution(12345)) # "11000000111001"
