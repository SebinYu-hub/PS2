#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# [실생활 예시] : [알고리즘 본질]
# 1. 자연 성장 패턴 : 재귀적 성장과 중복 계산 방지
# 2. 토끼 번식 예측 : 이전 세대 결과 재활용
# 3. 세포 분열 패턴 : 메모이제이션으로 계산 최적화
# 4. 재귀적 투자 수익 : 중복 계산 없는 복리 계산

# [코딩테스트 꿀팁]
# 1. 메모이제이션 초기화
#    memo = {}  # 딕셔너리 사용
#    memo = [0] * (n+1)  # 리스트 사용
# 
# 2. 기저 조건 처리
#    if n <= 1: return n
#    if n in memo: return memo[n]
#
# 3. 캐시 업데이트
#    memo[n] = fibo(n-1) + fibo(n-2)
#    return memo[n]

# 1. 알고리즘의 개념:
#    피보나치 수열은 첫 번째와 두 번째 항이 1이고, 그 이후의 항은 직전의 두 항의 합인 수열입니다.
#    이 알고리즘은 메모이제이션을 사용하여 이전에 계산한 값을 저장하고 재사용함으로써, 중복 계산을 방지하는 피보나치 재귀 알고리즘입니다.

# 2. 예시 입력 / 출력:
#    입력: 5
#    출력: 5 (피보나치 수열의 5번째 항은 5입니다)

# 3. 알고리즘의 시간 복잡도:
#    이 알고리즘의 시간 복잡도는 O(n)입니다. 메모이제이션 덕분에 각 n에 대해 계산은 한 번만 이루어집니다.

# 4. 해당 알고리즘으로 풀 수 있는 문제 예시:
#    - n 번째 피보나치 수 찾기
#    - 피보나치 수열을 사용하여 다양한 수학적 문제 해결

# 5. 상세 과정:
#    - n이 0이나 1인 경우, n을 반환합니다. (기저 사례)
#    - n이 메모 딕셔너리에 이미 키로 존재하면, 해당 값을 반환합니다.
#    - 그렇지 않으면, fibonacci(n-1)과 fibonacci(n-2)를 재귀적으로 호출하여 두 결과를 합칩니다. 그리고 이 값을 메모 딕셔너리에 저장한 후 반환합니다.
def fibonacci(n, memo={}):    
    if n <= 1:
        return n

    # 이미 계산된 값이면 메모에서 반환
    if n in memo:
        return memo[n]

    # 새로운 값 계산 후 메모에 저장
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

# 예제:
print(fibonacci(5))  # 출력: 5
