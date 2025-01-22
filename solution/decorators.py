import time
import functools
import logging
import inspect
import os
import re
from typing import Callable, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def get_category_from_filename(file_path: str) -> str:
    """파일 이름에서 카테고리를 추출"""
    file_name = os.path.basename(file_path)
    
    # 트리 관련 파일 처리
    if 'tree' in file_name.lower():
        return 'Tree'
    
    # 파일명에 카테고리가 명시된 경우 (예: sort_algorithms.py)
    if '_' in file_name:
        category = file_name.split('_')[0].capitalize()
        if category.isalpha():  # 알파벳으로만 구성된 경우
            return category
    
    # 난이도가 표시된 경우 (예: hard-트리순회.py)
    if '-' in file_name:
        difficulty = file_name.split('-')[0].capitalize()
        if difficulty in ['Easy', 'Medium', 'Hard']:
            return difficulty
    
    return 'Algorithm'  # 기본 카테고리

def get_problem_number(file_path: str) -> str:
    """파일 이름에서 문제 번호를 추출"""
    file_name = os.path.basename(file_path)
    
    # solution/24.py 형식 처리
    match = re.search(r'/(\d+)\.py$', file_path)
    if match:
        return match.group(1)
    
    # 파일명에서 숫자 추출
    numbers = re.findall(r'\d+', file_name)
    if numbers:
        return numbers[0]
    
    return file_name.split('.')[0]  # 기본값으로 파일명 사용

def algorithm_logger():
    """데코레이터: 알고리즘 실행 로그와 시간을 측정합니다."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            file_path = inspect.getfile(func)
            category = get_category_from_filename(file_path)
            
            logger = logging.getLogger(f'Algorithm.{category}')
            
            # 함수 시작 로깅
            logger.info(f"Starting algorithm: {func.__name__}")
            if args:
                logger.debug(f"Arguments: {args}")
            if kwargs:
                logger.debug(f"Keyword arguments: {kwargs}")
            
            # 시간 측정 시작
            start_time = time.time()
            
            try:
                result = func(*args, **kwargs)
                execution_time = time.time() - start_time
                logger.info(f"Algorithm {func.__name__} completed successfully in {execution_time:.4f} seconds")
                return result
            
            except Exception as e:
                logger.error(f"Error in algorithm {func.__name__}: {str(e)}")
                raise
            
        return wrapper
    return decorator

def solution_logger():
    """데코레이터: 문제 해결 과정의 로그와 시간을 측정합니다."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            file_path = inspect.getfile(func)
            problem_number = get_problem_number(file_path)
            
            logger = logging.getLogger(f'Solution.{problem_number}')
            
            # 문제 해결 시작 로깅
            if args:
                logger.debug(f"Input test case: {args}")
            if kwargs:
                logger.debug(f"Additional parameters: {kwargs}")
            
            # 시간 측정 시작
            start_time = time.time()
            
            try:
                result = func(*args, **kwargs)
                execution_time = time.time() - start_time
                
                # 모든 시간을 밀리초(ms)로 통일
                time_str = f"{execution_time * 1000:.3f} ms"
                
                logger.info(f"Solution completed successfully in {time_str}")
                logger.info(f"Result: {result}")
                return result
                
            except Exception as e:
                logger.error(f"Error in solution {func.__name__}: {str(e)}")
                raise
            
        return wrapper
    return decorator

# 사용 예시
if __name__ == "__main__":
    @algorithm_logger()  # solution/tree_traversal.py -> Category: Tree
    def traverse_tree(root):
        pass

    @solution_logger()  # solution/24.py -> Problem: 24
    def solve_problem(n: int) -> int:
        return n * 2 