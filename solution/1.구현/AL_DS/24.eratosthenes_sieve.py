#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# [실생활 예시] : [알고리즘 본질]
# 1. 암호화 키 생성 : 큰 소수 찾기
# 2. 소인수분해 : 소수들의 곱으로 분해
# 3. 수학 교육 : 소수의 분포 패턴 학습

# [코딩테스트 꿀팁]
# 1. 메모리 최적화
#    - bool 배열 사용
#    - 짝수는 미리 제외
# 2. 제곱근까지만 체크
#    - i*i <= n 조건으로 최적화
# 3. 구간 체 활용
#    - 특정 범위의 소수 찾기
#    - 메모리 효율적인 구현

def sieve_of_eratosthenes(n):
    # 소수 여부를 저장할 배열 초기화
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            # i의 배수들을 모두 제거
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    # 소수 목록 반환
    return [i for i in range(n + 1) if is_prime[i]]

# 예시 사용법
print(sieve_of_eratosthenes(30))  # 출력: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# 실제 활용 예시 - 구간 소수 찾기
def segment_sieve(left, right):
    # 구간 [left, right]에서 소수 찾기
    size = right - left + 1
    is_prime = [True] * size
    
    # 2부터 sqrt(right)까지의 소수로 체크
    for i in range(2, int(right ** 0.5) + 1):
        # left 이상의 i의 배수부터 시작
        start = max(i * i, ((left + i - 1) // i) * i)
        for j in range(start, right + 1, i):
            is_prime[j - left] = False
    
    # 결과 반환 (left가 1 이하인 경우 2 미만 제외)
    return [i + left for i in range(size) if is_prime[i] and i + left >= 2]

# 테스트
print(segment_sieve(10, 20))  # 출력: [11, 13, 17, 19]
