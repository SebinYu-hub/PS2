#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 문자열을 숫자로 변환하는 알고리즘은 문자열 형태의 숫자를 실제 정수 또는 실수 형태로 변환하는 알고리즘입니다.
# Python에서는 int() 함수를 사용하여 문자열을 정수로, float() 함수를 사용하여 문자열을 실수로 변환할 수 있습니다.

# [실생활 예시] : [알고리즘 본질]
# 1. 웹 폼 데이터 처리 : 사용자 입력 문자열을 숫자로 변환
# 2. 파일 데이터 파싱 : CSV 파일의 문자열 데이터를 숫자로 변환
# 3. 계산기 구현 : 문자열 형태의 수식을 계산 가능한 숫자로 변환

# [코딩테스트 꿀팁]
# 1. 예외 처리 필수
#    - try-except로 변환 실패 처리
#    - isdigit()으로 사전 검사
# 2. 진수 변환 활용
#    - int('1010', 2): 2진수 문자열을 10진수로
#    - hex(), oct(), bin(): 진수 변환
# 3. 실수 처리 주의
#    - float 변환 시 정밀도 손실 가능
#    - decimal 모듈 고려

def string_to_number(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return "변환 불가"

# 예시 사용법
print(string_to_number("123"))  # 출력: 123

# 실제 활용 예시 - 다양한 형태의 문자열 변환
def advanced_conversion(s):
    # 숫자 문자열인지 확인
    if s.isdigit():
        return int(s)
    
    # 16진수 확인 (0x로 시작)
    if s.startswith('0x'):
        try:
            return int(s, 16)
        except ValueError:
            pass
    
    # 2진수 확인 (0b로 시작)
    if s.startswith('0b'):
        try:
            return int(s, 2)
        except ValueError:
            pass
    
    # 실수 확인
    try:
        return float(s)
    except ValueError:
        return "변환 불가"

# 테스트
print(advanced_conversion("0xFF"))     # 출력: 255
print(advanced_conversion("0b1010"))   # 출력: 10
print(advanced_conversion("3.14"))     # 출력: 3.14
print(advanced_conversion("abc"))      # 출력: 변환 불가
