#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 에러 메시지: TypeError: can only concatenate str (not "int") to str
# 의미: 문자열과 숫자는 서로 더할 수 없으며, 이렇게 시도할 때 이 에러가 발생합니다.

# 에러 발생 코드
result = "string" + 123

# 해결 방법:
# 숫자를 문자열로 변환하여 오류를 방지할 수 있습니다.
# 예:
# result = "string" + str(123)
