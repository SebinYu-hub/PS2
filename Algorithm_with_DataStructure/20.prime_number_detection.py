#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 소수 판별 알고리즘은 주어진 숫자가 소수인지 아닌지를 판별하는 알고리즘입니다.
# 소수는 1과 자기 자신 이외에 어떠한 수로도 나누어 떨어지지 않는 1보다 큰 양의 정수를 의미합니다.
# 이 알고리즘은 2부터 (입력받은 숫자의 제곱근 + 1)까지의 숫자로 나누어 볼 때,
# 한 번이라도 나누어 떨어지면 소수가 아니며, 모두 나누어 떨어지지 않으면 소수입니다.

# [실생활 예시] : [알고리즘 본질]
# 1. 암호화 시스템 : RSA 암호화에서 큰 소수 찾기
# 2. 해시 테이블 크기 : 충돌을 줄이기 위한 소수 크기 선택
# 3. 난수 생성 : 소수를 이용한 의사 난수 생성

# [코딩테스트 꿀팁]
# 1. 제곱근까지만 검사
#    - n의 약수는 √n을 기준으로 대칭
#    - O(√n)으로 시간복잡도 개선
# 2. 에라토스테네스의 체와 비교
#    - 단일 수 검사: is_prime()
#    - 범위 내 소수: 에라토스테네스의 체
# 3. 2부터 시작
#    - 1은 소수가 아님을 주의

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 예시 사용법
print(is_prime(7))  # 출력: True

# 실제 활용 예시 - 범위 내 소수 개수 세기
def count_primes_in_range(start, end):
    return sum(1 for n in range(start, end+1) if is_prime(n))

# 1부터 20까지의 소수 개수
print(count_primes_in_range(1, 20))  # 출력: 8 (2,3,5,7,11,13,17,19)

# 소수들의 리스트 생성
primes = [n for n in range(2, 30) if is_prime(n)]
print(primes)  # 출력: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
