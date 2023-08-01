# install vscode keymap -> apply
# bubble sort : 인접한 두 요소를 비교하여 큰 값을 오른쪽으로 이동시키는 과정을 반복

"""
numbers = [63, 31, 27, 11, 25]


def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


bubble(numbers)
print(numbers)
"""

# debugger
# breaking point : usually to called function -> debug : F5 -> step into : F11 -> step over : F10 -> stop : Shift + F5

# counting sort : 정수를 정렬하는 알고리즘, 각 숫자의 개수를 세어서 정렬

"""
def counting(arr):
    max_value = max(arr)
    # list for count
    count_arr = [0] * (max_value + 1)

    for num in arr:
        count_arr[num] += 1

    sorted_arr = []
    for i, count in enumerate(count_arr):  # index, value pair
        sorted_arr.extend([i] * count)  # iterable -> extend

    return sorted_arr


num_list = [1, 4, 1, 2, 7, 5, 2]
sorted_list = counting(num_list)
print(sorted_list)
"""

# permutation : 주어진 항목들로 만들 수 있는 모든 가능한 순서 (튜플)

# permutation by itertools module

"""
import itertools

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(itertools.permutations(arr))
print(result)
"""

# greedy algorithm : 각 단계에서 가장 최선의 선택을 하는 방법
# 거스름돈을 줄 때 가장 적은 수의 동전을 사용하여 거스름돈을 주는 문제
# 최선의 선택 : 가장 큰 단위의 동전부터 사용하는 것
# 실습 : 동전 종류가 100원, 50원, 10원 거스름돈이 380원이라면 어떻게 해야 가장 적은 수의 동전으로 거스름돈을 받을 수 있을까요?

"""
def greedy(money, coins):
    coins.sort(reverse=True)
    # dictionary for change
    change = {coin: 0 for coin in coins}
    for coin in coins:
        while money >= coin:
            money -= coin
            # for each calculation coin plus one
            change[coin] += 1
    return change


result = greedy(380, [100, 50, 10])
print(result)    
"""

"""
T = int(input())

for i in range(1, T + 1):
    N = int(input())
    cards = input()
    # 숫자의 등장 횟수를 저장할 딕셔너리 생성
    counts = {str(n): 0 for n in range(10)}
    # 각 숫자의 등장횟수를 세기
    for card in cards:
        counts[card] += 1
    max_count = max(counts.values())
    # max_count 와 같은 횟수를 가진 숫자들 중 가장 큰 숫자를 찾는다.
    max_number = max([int(num) for num, count in counts.items() if count == max_count])
    print(f"#{i} {max_number} {max_count}")
"""

"""
T = int(input())

for i in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    new_arr = []

    for j in range(N - M + 1):
        result = 0
        # j 부터 j + M 까지의 합
        for k in range(j, j + M):
            result += arr[k]
        new_arr.append(result)
    max_arr = max(new_arr)
    min_arr = min(new_arr)
    print(f"#{i} {max_arr - min_arr}")
"""

"""
T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())  # K : 정류장수, N : 종점, M : 충전기 설치된 정류장 수
    arr = list(map(int, input().split()))
    curr, cnt = 0, 0
    # 종점 도착 할 때까지 반복
    while curr != N:
        # curr + K : 한 번 충전으로 갈 수 있는 거리, N : 종점까지 거리
        if N <= curr + K:
            curr = N
            break
        # 충전소 뒤에서부터 순환
        for i in range(len(arr) - 1, -1, -1):
            # 라스트 arr 의 값이 curr + K 거리 이내에 있다면
            if arr[i] <= curr + K:
                cnt += 1  # 충전 횟수 증가
                curr = arr[i]  # 현재 위치를 충전소 위치로 변경
                arr = arr[i + 1:] # 해당 충전소 이후의 정류장만 남기기
                break
            # 충전소를 찾지 못하였다면
            if i == 0:
                cnt = 0
                curr = N  # 현재 위치를 종점으로
    print(f"#{tc} {cnt}")
"""
