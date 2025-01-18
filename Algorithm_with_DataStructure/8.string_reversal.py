#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 문자열 뒤집기는 주어진 문자열의 문자들의 순서를 반대로 만드는 알고리즘입니다.
# Python에서는 문자열 슬라이싱을 이용해 이를 간단히 구현할 수 있으며,
# s[::-1] 형태로 사용하면 문자열 s를 뒤집어 줍니다.

# [실생활 예시] : [알고리즘 본질]
# 1. 회문 검사 : 앞뒤로 같은 단어/문장 확인
# 2. 문자열 암호화 : 단순한 문자열 변환 암호화
# 3. 텍스트 미러링 : 거울에 비친 것처럼 텍스트 반전

# [코딩테스트 꿀팁]
# 1. 슬라이싱 활용
#    - s[::-1]: 가장 빠르고 간단
#    - reversed(s): 메모리 효율적
# 2. 투 포인터 방식
#    - 양 끝에서 시작해서 중앙으로
#    - 리스트 형태에서 유용
# 3. join과 함께 사용
#    - ''.join(reversed(s))
#    - 문자 단위 처리 필요시

def reverse_string(s):
    return s[::-1]

# 예시 사용법
print(reverse_string("Hello"))  # 출력: "olleH"

# 실제 활용 예시 - 다양한 방법으로 문자열 뒤집기
# 1. 투 포인터 방식
def reverse_string_two_pointer(s):
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)

# 2. 단어 단위로 뒤집기
def reverse_words(s):
    return ' '.join(word[::-1] for word in s.split())

# 테스트
text = "Hello World"
print(reverse_string_two_pointer(text))  # 출력: "dlroW olleH"
print(reverse_words(text))              # 출력: "olleH dlroW"
