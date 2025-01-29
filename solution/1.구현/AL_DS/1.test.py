from itertools import combinations, permutations, combinations_with_replacement

arr = [1,2,3,4]

print(combinations(arr, 2))

print(list(combinations(arr, 2))) #list - comb 필수

print(list(permutations(arr, 2))) # permutations - (1,2) (2,1) 순서가 다르기만한거 포함

print(list(combinations_with_replacement(arr, 2))) # (1,1) (2,2)중복 허용