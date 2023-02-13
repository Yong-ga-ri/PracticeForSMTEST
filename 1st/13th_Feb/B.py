from itertools import combinations  # permutations

N, M = map(int, input().split())  # n, m 입력
input_numbers = list(map(int, input().split()))  # 수 입력

combi_result = list(combinations(input_numbers, M))  # 조합


print(combi_result)

combi_result.sort(key=lambda x: (x[0], x[1]))  # 원소들 오름차순으로 정렬

# TODO 새로운 리스트 초기화
sorted_list = []

for i in combi_result:
    sorted_list.append([i[1], i[0]])

for i in sorted_list:
    print(*i)
