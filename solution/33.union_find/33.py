"""
[Input]
1. k: int
   - 초기 집합의 개수
   - 각 집합은 0부터 k-1까지의 단일 원소로 시작

2. operations: List[List[Union[str, int]]]
   - 연산 목록
   - ["u", a, b]: a가 속한 집합과 b가 속한 집합을 합침
   - ["f", a]: a가 속한 집합의 대표 원소 찾기

[Output]
- result: int
  - 모든 연산 수행 후 존재하는 집합의 개수
  - 같은 대표 원소를 갖는 원소들은 같은 집합
"""

"""
[문제 특징] : [알고리즘 선택 이유]
1. 집합 병합 연산 필요 : Union-Find 자료구조 선택
2. 대표 원소 조회 빈번 : 경로 압축으로 find 최적화
3. 동적 집합 관리 : 부모 배열로 효율적 관리
4. 집합 개수 카운팅 : 유니크한 루트 노드 개수 계산
5. 반복적 연산 처리 : 연산별 분기 처리
"""

"""
[자료구조]
1. parents: List[int]
   - 각 원소의 부모 노드 저장
   - parents[i] = i면 루트 노드
   - 경로 압축으로 최적화

2. operations: List[List[Union[str, int]]]
   - 연산 정보 저장
   - union: 두 집합 병합
   - find: 집합 대표 원소 조회

[알고리즘: Union-Find with Path Compression]
procedure process_operations(k, operations):
    1. Initialize:
       - parents 배열 생성
       - 각 원소를 독립 집합으로 설정
    
    2. Process Operations:
       - union: 두 집합 병합
       - find: 경로 압축하며 루트 찾기
    
    3. Return 유니크한 루트 노드 개수
"""

def find(parents, x):
    # 최적화 1: 경로 압축을 통한 find 연산
    # 재귀적으로 루트를 찾으면서 모든 노드가 직접 루트를 가리키도록 설정
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    # 최적화 2: Union by Rank 대신 간단한 방식 사용
    # 두 집합을 합칠 때 항상 첫 번째 집합에 두 번째 집합을 포함
    root1 = find(parents, x)
    root2 = find(parents, y)
    if root1 != root2:  # 최적화 3: 불필요한 할당 방지
        parents[root2] = root1

def solution(k, operations):
    # 부모 배열 초기화: 각 노드는 자기 자신을 부모로 가짐
    parents = list(range(k))
    
    # 연산 처리
    for op in operations:
        if op[0] == "u":  # union 연산
            union(parents, op[1], op[2])
        else:  # find 연산
            find(parents, op[1])
    
    # 최적화 4: set comprehension으로 유니크한 루트 개수 계산
    return len({find(parents, i) for i in range(k)})

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution(3,[['u', 0, 1], ['u', 1, 2], ['f', 2]])) # 반환값 : 1
# print(solution(4,[['u', 0, 1], ['u', 2, 3], ['f', 0]])) # 반환값 : 2
