#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 시간 측정 알고리즘은 코드의 실행 시간을 측정하는 알고리즘입니다.
# Python의 time 모듈을 사용하여 특정 코드 블록 또는 함수의 실행 시간을 측정할 수 있습니다.

import time
from functools import wraps

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"실행 시간: {end_time - start_time}초")
        return result
    return wrapper

# 예시 사용법
@measure_time
def sample_function():
    for _ in range(1000000):
        pass

sample_function()  # 출력: 실행 시간(초)
