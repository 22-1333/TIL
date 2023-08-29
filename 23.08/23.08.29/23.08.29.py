# 슬라이딩 윈도우
# 1. 주로 리스트와 같은 시퀀스 타입에서 일정 크기의 윈도우를 정한다.
# 2. 그 윈도우를 데이터의 처음부터 끝까지 움직이면서 해결한다.
"""
n개의 정수를 입력 받고, 연속된 m개의 정수들의 합을 구할 때 최대 값 구하기
합이 가장 큰 구간의 값은 무엇일까요? (2 <= m, n <= 100,000)

input
10 2
3 -2 -4 -9 0 3 7 13 8 -3

output
21

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum_value = 0
for i in range(m):
    sum_value += arr[i]
    max_v = sum_value
for i in range(n - m):
    sum_value += arr[i + m]
    sum_value -= arr[i]
    if sum_value > max_v:
        max_v = sum_value
print(max_v)
"""

# 투 포인터
# 주로 리스트와 같은 시퀀스 타입에서 두 개의 포인터를 사용하여 문제를 풀이하는 방법
"""
1 부터 10,000 사이의 n개의 자연수 중에서 연속된 숫자를 더했을 때 합이 m이 되는 경우는 몇 가지 인가요?
(투 포인터 -> 구간의 크기가 정해지지 않았을 때)

input
10 5
1 2 3 4 2 5 3 1 1 2

output
3

n, target = map(int, input().split())
arr = list(int, input().split())
cnt, sum = 0, 0
# 투 포인터 high, low
high, low = 0, 0
while True:
    if sum >= target or high == n:
        sum -= arr[low]
        low += 1
    elif sum < target:
        sum += arr[high]
        high += 1
    if sum == target:
        cnt += 1
    if low == n:
        break
print(cnt)
"""

# 18672

"""
n, m = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
sum, cnt = 0, 0

while right <= n:
    if sum < m:
        if right < n:
            sum += arr[right]
        right += 1
    if sum > m:
        sum -= arr[left]
        left += 1
    if sum == m:
        cnt += 1
        if right < n:
            sum += arr[right]
        right += 1
print(cnt)
"""

# 18673

"""
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    start = 0
    end = m - 1
    midsum = sum(arr[:end])
    ans = -999999
    s_index = 0
    e_index = 0
    while end < n:
        midsum += arr[end]
        if midsum > ans:
            ans = midsum
            s_index = start
            e_index = end
        midsum -= arr[start]
        start += 1
        end += 1
    print(f"#{tc} {s_index} {e_index} {ans}")
"""

# 18674

"""
minimum = 2e9 + 1
ansleft = 0
ansright = 0
while left < right:
    sum = arr[left] + arr[right]
    if sum == 0:
        if abs(arr[left] + arr[right]) > max_sum:
            ansleft = left
            ansright = right
            max_sum = abs(arr[left] + arr[right])
        print(arr[left], arr[right])
        exit()
    if minimum > abs(sum):
        minimum = abs(sum)
        ansleft = left
        ansright = right
    if sum > 0:
        right -= 1
    else:
        left += 1
print(arr[ansleft], arr[ansright])
"""
