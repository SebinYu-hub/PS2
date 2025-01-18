"""
[Input]
1. func: function
   - 측정할 대상 함수
   - 제약: 호출 가능한 함수 객체

[Output]
- result: float
  - 함수의 실행 시간(초)
  - 제약: result >= 0
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 함수 실행 시간 측정 필요 : time.time() 활용
2. 함수 수정 없이 기능 추가 : 데코레이터 패턴 적용
3. 예외 상황 처리 필요 : try-except 구문 사용
4. 메타데이터 보존 필요 : functools.wraps 활용
5. 정밀한 시간 측정 필요 : 시스템 시간 활용
"""
"""
[자료구조]
- start_time, end_time: float
  - 목적: 함수 실행 시작/종료 시간 저장
  - 특징: 시스템 시간 기반 정밀도

[알고리즘: Function Execution Time Measurement]
procedure measure_time(func):
    1. Create wrapper function:
       - 원본 함수의 메타데이터 보존
       - 파라미터 전달 지원
    
    2. Inside wrapper:
       - 시작 시간 기록
       - 원본 함수 실행
       - 종료 시간 기록
       - 실행 시간 계산
    
    3. Handle exceptions:
       - 시간 측정 오류 처리
       - 음수 시간 검증
    
    4. Return 실행 시간
"""

import time
from functools import wraps


@staticmethod
def measure_time(func):
    @wraps(func)  # 원본 함수의 메타데이터 보존
    def wrapper(*args, **kwargs):
        try:
            start_time = time.time()  # 시작 시간 기록
            result = func(*args, **kwargs)  # 함수 실행
            end_time = time.time()    # 종료 시간 기록
            execution_time = end_time - start_time
            
            # 음수 시간 체크 (시스템 시간이 변경된 경우 등)
            if execution_time < 0:
                raise ValueError("Invalid execution time")
                
            return execution_time
        except Exception as e:
            print(f"Error measuring time: {e}")
            return None
            
    return wrapper

# 사용 예시:
@measure_time
def example_function():
    time.sleep(1)  # 1초 대기

print(example_function())  # 약 1초의 실행 시간 출력