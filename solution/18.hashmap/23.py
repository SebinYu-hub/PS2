"""
[Input]
1. genres: list[str]
   - 노래의 장르 배열
   - 제약: 1 ≤ len(genres) ≤ 10,000
   - 제약: 장르는 100개 미만

2. plays: list[int]
   - 노래의 재생 횟수 배열
   - 제약: len(plays) == len(genres)
   - 제약: 1 ≤ plays[i] ≤ 10,000

[Output]
- result: list[int]
  - 베스트 앨범에 수록할 노래의 고유번호 배열
  - 제약: 장르별 최대 2곡까지 수록
  - 제약: 장르 내에서는 재생 횟수 내림차순
  - 제약: 재생 횟수가 같으면 고유번호 오름차순
"""
"""
[문제 특징] : [알고리즘 선택 이유]
1. 그룹화 필요 : defaultdict로 장르별 곡 관리
2. 다중 정렬 필요 : 튜플로 정렬 키 구성
3. 장르 우선순위 필요 : 총 재생수로 장르 정렬
4. 곡 선택 필요 : 장르당 최대 2곡 선택
5. 인덱스 유지 필요 : 곡의 고유번호 보존
"""
"""
[자료구조]
1. genre_songs: defaultdict(list)
   - 목적: 장르별 곡 정보 저장
   - 특징: (재생수, -인덱스) 튜플로 저장
   - 연산: append, sort

2. genre_total_plays: defaultdict(int)
   - 목적: 장르별 총 재생수 저장
   - 특징: 장르 우선순위 결정
   - 연산: 누적 합계

[알고리즘: Best Album]
procedure solution(genres, plays):
    1. Group songs:
       - 장르별로 곡 정보 수집
       - 장르별 총 재생수 계산
    
    2. Sort genres:
       - 총 재생수로 장르 정렬
       - 내림차순 정렬
    
    3. Select songs:
       - 각 장르에서 최대 2곡 선택
       - 재생수 내림차순, 인덱스 오름차순
"""

from collections import defaultdict

def solution(genres, plays):
    # 장르별 곡 정보를 저장할 defaultdict
    genre_songs = defaultdict(list)
    genre_total_plays = defaultdict(int)
    
    # 장르별로 곡 정보 수집
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_songs[genre].append((play, -i))  # 재생 수와 고유번호(음수로 저장하여 큰 번호 우선)
        genre_total_plays[genre] += play
    
    answer = []
    # 1. 장르 순서 결정 (총 재생수 기준 내림차순)
    for genre in sorted(genre_total_plays, key=genre_total_plays.get, reverse=True):
        # 2. 장르 내 곡 선택 (재생수 내림차순, 고유번호 오름차순)
        songs = sorted(genre_songs[genre], reverse=True)[:2]
        # 고유번호 복원하여 결과 추가
        answer.extend(-song[1] for song in songs)
    
    return answer

# 예시 실행
# genres = ["classic", "pop", "classic", "classic", "pop"]
# plays = [500, 600, 150, 800, 2500]
# print(solution(genres, plays))  # [4, 1, 3, 0]
