# 해쉬

from collections import Counter, defaultdict

hash = {'a': 1}

print(hash.get('b'))
# print(hash['b']) #keyerror - 그냥 이거 안쓰면 되는건가

print(hash.pop('a')) # val 리턴 + 둘다 out

from collections import Counter

#iterater = str
str = "heheheheheQQQQqq2"
#dict + Counter 조합 필수
print(dict(Counter(str)))